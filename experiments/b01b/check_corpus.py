"""B01b fixed-corpus research checks, not an importer or complete schema validator.

No arguments, arbitrary roots, path-driven reads, networking or normalized output.
Semantic variants operate on parsed copies AFTER the fixed raw integrity check.
"""
from copy import deepcopy
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import sys


FILES = {
    "updated": "events-updated.json", "deleted": "events-deleted.json",
    "handlers": "handlers.jsonl", "attempts": "attempts.jsonl",
    "snapshots": "snapshots.jsonl", "meta": "metadata.json",
    "manifest": "manifest.json", "expected": "expected.json", "variants": "variants.json",
}
COLLECTIONS = {"stripe_events": "events", "delivery_attempts": "attempts",
               "handler_observations": "handlers", "state_snapshots": "snapshots"}
FIELDS = {"access", "status", "cancellationTombstone", "processedEventCount", "mutationCount"}
STATUSES = {"incomplete", "incomplete_expired", "trialing", "active", "past_due",
            "canceled", "unpaid", "paused"}
ROWS = {
    "attempts": set("rowId producerNamespace eventId endpointId providerAttemptId requestId sentAt receivedAt arrival httpStatus transport retryOfAttemptRef".split()),
    "handlers": set("rowId producerNamespace executionId eventId attemptRef requestId subscriptionId observedAt phase transactionId errorCode".split()),
    "snapshots": set("rowId producerNamespace subscriptionId capturedAt storeId readKind transactionId executionId valuesSchema values absentFields".split()),
}


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def parse(raw):
    return json.loads(raw, object_pairs_hook=unique_object,
                      parse_constant=lambda value: require(False, "nonfinite JSON"))


def pointer(document, text):
    if text == "":
        return document
    require(text.startswith("/") and not re.search(r"~(?![01])", text), "pointer syntax")
    parts = text[1:].split("/")
    if isinstance(document, list) and parts[0] == "line":
        require(len(parts) >= 2 and re.fullmatch(r"[1-9][0-9]*", parts[1]), "line pointer")
        document, parts = document[int(parts[1]) - 1], parts[2:]
    for part in parts:
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(document, list):
            require(re.fullmatch(r"0|[1-9][0-9]*", part), "array pointer")
            document = document[int(part)]
        else:
            document = document[part]
    return document


def safe_count(value):
    return type(value) in (int, float) and 0 <= value <= 9007199254740991 and value == int(value)


def time(value):
    if value is None:
        return None
    require(isinstance(value, str) and re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d{3}Z", value), "time syntax")
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")


def integrity(raw, manifest, expected):
    errors = set()
    for source in manifest["sources"]:
        # IDs address an already-read dictionary. Source.path is never opened.
        data = raw[source["id"]]
        if source["bytes"] != len(data) or source["sha256"] != hashlib.sha256(data).hexdigest():
            errors.add("fatal:HASH_MISMATCH")
    identity = expected["manifestIdentity"]
    if identity != {"bytes": len(raw["manifest"]), "sha256": hashlib.sha256(raw["manifest"]).hexdigest()}:
        errors.add("fatal:MANIFEST_IDENTITY")
    return errors


def inspect(bundle):
    """Targeted contract predicates for this finite corpus; no publication API."""
    errors = set()
    def check(ok, code):
        if not ok:
            errors.add("fatal:" + code)

    def ref(value):
        try:
            require(set(value) == {"sourceId", "pointer"}, "ref fields")
            require(value["sourceId"] in sources, "ref source")
            return pointer(bundle[value["sourceId"]], value["pointer"])
        except (AssertionError, KeyError, IndexError, TypeError, ValueError):
            check(False, "REFERENCE_INVALID")
            return None

    def namespace(value):
        if value is None:
            return
        check(set(value) == {"application", "deployment", "domain", "basis", "refs"}, "NAMESPACE")
        check(value.get("basis") in {"source_asserted", "operator_mapping"}, "NAMESPACE")
        triple = {k: value.get(k) for k in ("application", "deployment", "domain")}
        check(all(isinstance(v, str) and v for v in triple.values()), "NAMESPACE")
        citations = [ref(r) for r in value.get("refs", [])]
        # Corpus uses whole captured namespace triples, not arbitrary mapping prose.
        check(bool(citations) and all(isinstance(c, dict) and all(c.get(k) == v for k, v in triple.items()) for c in citations), "NAMESPACE_CITATION")

    manifest = bundle["manifest"]
    check(set(manifest) == {"schemaVersion", "bundleId", "sources", "scopes", "mappings"}, "MANIFEST_SHAPE")
    check(manifest["schemaVersion"] == "hooktrace.input/1", "SCHEMA_UNSUPPORTED")
    sources = {s["id"]: s for s in manifest["sources"]}
    scopes = {s["id"]: s for s in manifest["scopes"]}
    check(len(sources) == len(manifest["sources"]), "DUPLICATE_SOURCE")
    check(len(scopes) == len(manifest["scopes"]), "DUPLICATE_SCOPE")
    for source in manifest["sources"]:
        path = source["path"]
        check(isinstance(path, str) and bool(path) and not path.startswith("/")
              and not any(p in {"", ".", ".."} for p in path.split("/"))
              and "\\" not in path and "\0" not in path, "PATH_INVALID")
        check(source["kind"] in {*COLLECTIONS, "scope_metadata"}, "SOURCE_SHAPE")
        check(source["format"] in {"json", "jsonl"}, "SOURCE_SHAPE")
        check(safe_count(source["bytes"]) and isinstance(source["sha256"], str)
              and re.fullmatch(r"[0-9a-f]{64}", source["sha256"]), "SOURCE_SHAPE")
    for scope in scopes.values():
        value, coverage = scope["value"], scope["coverage"]
        check(set(value) == {"accountId", "environment", "environmentId", "context"}, "SCOPE_SHAPE")
        check(value["environment"] in {"live", "test", "unknown"}, "SCOPE_SHAPE")
        check(all(v is None or isinstance(v, str) and v for k, v in value.items() if k != "environment"), "SCOPE_SHAPE")
        if value["accountId"] is None or value["environment"] == "unknown" or value["environmentId"] is None:
            errors.add("insufficient:scope")
        origin = scope["origin"]
        check(bool(origin["refs"]), "SCOPE_CITATION")
        for citation in origin["refs"]:
            captured = ref(citation)
            if origin["method"] == "source_field":
                check(captured == value, "SCOPE_CITATION")
        check(origin["method"] in {"source_field", "declared_mapping"}, "SCOPE_CITATION")
        if origin["method"] == "declared_mapping":
            check(origin["mappingId"] in {m["id"] for m in manifest["mappings"]}, "MAPPING_INVALID")
        try:
            start, end = time(coverage["start"]), time(coverage["end"])
            check(start is None or end is None or start <= end, "COVERAGE")
        except (AssertionError, ValueError):
            check(False, "COVERAGE")
        check(coverage["completeness"] in {"partial", "source_claimed_complete", "unknown"}, "COVERAGE")
        for citation in coverage["refs"]:
            captured = ref(citation)
            check(isinstance(captured, dict) and all(captured.get(k) == coverage[k] for k in ("start", "end", "completeness")), "COVERAGE_CITATION")
    mappings = manifest["mappings"]
    mapping_fields = {"id", "sourceId", "scopeId", "adapter", "recordsPointer", "declaredApiVersion"}
    if any(set(m) != mapping_fields for m in mappings):
        check(False, "MAPPING_INVALID")
        return errors, [], []
    check(len({m["id"] for m in mappings}) == len(mappings), "MAPPING_INVALID")
    for source in sources.values():
        selected = [m for m in mappings if m["sourceId"] == source["id"]]
        check(len(selected) == (0 if source["kind"] == "scope_metadata" else 1), "MAPPING_INVALID")
    row_index, assigned, keys = {}, {}, []
    for mapping in mappings:
        sid = mapping["sourceId"]
        if sid not in sources or mapping["scopeId"] not in scopes:
            check(False, "MAPPING_INVALID")
            continue
        source = sources[sid]
        collection = COLLECTIONS.get(source["kind"])
        check(mapping["adapter"] == ("stripe_snapshot_v1" if collection == "events" else "normalized_v1"), "MAPPING_INVALID")
        check(collection == "events" or mapping["declaredApiVersion"] is None, "MAPPING_INVALID")
        if collection is None:
            continue
        try:
            check(source["format"] != "jsonl" or mapping["recordsPointer"] == "", "MAPPING_INVALID")
            rows = pointer(bundle[sid], mapping["recordsPointer"])
            require(isinstance(rows, list), "array required")
        except (AssertionError, KeyError, IndexError, TypeError):
            check(False, "MAPPING_INVALID")
            continue
        scope = scopes[mapping["scopeId"]]["value"]
        for n, row in enumerate(rows):
            location = f"/line/{n + 1}" if source["format"] == "jsonl" else mapping["recordsPointer"] + f"/{n}"
            keys.append([sid, location, collection])
            if collection == "events":
                for observed, declared_value in ((row.get("account"), scope["accountId"]),
                                                  (row.get("context"), scope["context"])):
                    check(observed is None or declared_value is None or observed == declared_value, "SCOPE_CONFLICT")
                mode = row.get("livemode")
                if mode is not None:
                    check(type(mode) is bool, "EVENT_SHAPE")
                    check(scope["environment"] == "unknown" or ("live" if mode else "test") == scope["environment"], "SCOPE_CONFLICT")
                if row.get("object") == "v2.core.event":
                    errors.add("unsupported:thin")
                    continue
                version = row.get("api_version")
                declared = mapping["declaredApiVersion"]
                check(version is None or declared is None or version == declared, "VERSION_CONFLICT")
                if version != "2025-02-24.acacia":
                    errors.add("unsupported:version")
                    continue
                if row.get("type") not in {"customer.subscription." + t for t in ("created", "updated", "deleted")}:
                    errors.add("unsupported:type")
                    continue
                obj = row.get("data", {}).get("object", {})
                customer = obj.get("customer")
                customer_id = customer.get("id") if isinstance(customer, dict) else customer
                if not row.get("id") or not obj.get("id") or not customer_id:
                    errors.add("insufficient:identity")
                check(row.get("object") == "event" and obj.get("object") == "subscription", "EVENT_SHAPE")
                check(safe_count(row.get("created")), "EVENT_SHAPE")
                mode = obj.get("livemode")
                if mode is not None:
                    check(type(mode) is bool, "EVENT_SHAPE")
                    check(scope["environment"] == "unknown" or ("live" if mode else "test") == scope["environment"], "SCOPE_CONFLICT")
                if isinstance(customer, dict):
                    check(customer.get("object") == "customer" and ("deleted" not in customer or customer["deleted"] is True), "EVENT_SHAPE")
                continue
            check(set(row) == ROWS[collection], "ROW_SHAPE")
            label = row.get("rowId")
            check(isinstance(label, str) and bool(re.fullmatch(r"[A-Za-z0-9_.:-]{1,128}", label)), "ROW_SHAPE")
            check((sid, label) not in row_index, "DUPLICATE_ROW")
            row_index[sid, label] = (collection, row)
            assigned[sid, label] = scope
            namespace(row.get("producerNamespace"))
            for name in ("requestId", "executionId", "transactionId", "storeId"):
                local = row.get(name)
                if local is not None:
                    check(set(local) == {"value", "namespace"} and isinstance(local["value"], str) and bool(local["value"]), "LOCAL_ID")
                    namespace(local.get("namespace"))
            for name in ("sentAt", "receivedAt", "observedAt", "capturedAt"):
                try:
                    time(row.get(name))
                except (AssertionError, ValueError):
                    check(False, "TIME_INVALID")
            if collection == "attempts":
                status = row.get("httpStatus")
                check(status is None or safe_count(status) and 100 <= status <= 599, "ATTEMPT_SHAPE")
                check(row.get("transport") in {"response", "timeout", "connection_error", "unknown"}, "ATTEMPT_SHAPE")
                if row.get("arrival") is not None:
                    check(safe_count(row["arrival"]["index"]), "ATTEMPT_SHAPE")
                    namespace(row["arrival"]["streamId"]["namespace"])
            elif collection == "handlers":
                check(row.get("phase") in {"started", "completed", "failed", "write_claimed"}, "ROW_SHAPE")
            elif collection == "snapshots":
                check(isinstance(row.get("subscriptionId"), str) and bool(row["subscriptionId"]) and row.get("storeId") is not None, "ROW_SHAPE")
                check(row.get("readKind") in {"persisted_read", "transactional_read", "unknown"}, "ROW_SHAPE")
                check(row.get("valuesSchema") == "hooktrace.subscription-state/1", "VALUES_SCHEMA")
                values, absent = row["values"], row["absentFields"]
                if not isinstance(values, dict) or not isinstance(absent, list) or not all(isinstance(k, str) for k in absent):
                    check(False, "SNAPSHOT_SHAPE")
                    continue
                check(set(values) <= FIELDS, "SNAPSHOT_FIELD")
                check(set(absent) <= FIELDS and len(set(absent)) == len(absent) and not set(values).intersection(absent), "ABSENT_FIELDS")
                for name, value in values.items():
                    valid = (type(value) is bool if name in {"access", "cancellationTombstone"}
                             else isinstance(value, str) and value in STATUSES if name == "status"
                             else safe_count(value) if name in {"processedEventCount", "mutationCount"} else False)
                    check(valid, "SNAPSHOT_VALUE")
    resolved, retries = [], {}
    for key, (collection, row) in row_index.items():
        target = row.get("attemptRef" if collection == "handlers" else "retryOfAttemptRef")
        if target is None:
            continue
        destination = target.get("sourceId"), target.get("rowId")
        if set(target) != {"sourceId", "collection", "rowId"} or target.get("collection") != "attempts" or destination not in row_index or row_index[destination][0] != "attempts":
            check(False, "REFERENCE_INVALID")
            continue
        other = row_index[destination][1]
        resolved.append([*key, *destination])
        for name in ("eventId", "endpointId", "producerNamespace"):
            a, b = row.get(name), other.get(name)
            if name == "producerNamespace" and a is not None and b is not None:
                a, b = [a[k] for k in ("application", "deployment", "domain")], [b[k] for k in ("application", "deployment", "domain")]
            check(a is None or b is None or a == b, "REFERENCE_CONFLICT")
        for name in ("accountId", "environment", "environmentId", "context"):
            a, b = assigned[key][name], assigned[destination][name]
            check(a in (None, "unknown") or b in (None, "unknown") or a == b, "REFERENCE_CONFLICT")
        if collection == "attempts":
            retries[key] = destination
    for start in retries:
        seen, current = set(), start
        while current in retries:
            if current in seen:
                check(False, "RETRY_CYCLE")
                break
            seen.add(current)
            current = retries[current]
    return errors, keys, resolved


def exact(a, b):
    # JSON booleans must not compare equal to numeric 0/1 in expected facts.
    return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def facts(bundle, expected):
    for fact in expected["facts"]:
        require(exact(pointer(bundle[fact["sourceId"]], fact["pointer"]), fact["value"]), fact["meaning"])
    errors, keys, resolved = inspect(bundle)
    require(not errors, f"positive errors: {sorted(errors)}")
    require(keys == expected["observationKeys"], "observation origins")
    require(resolved == expected["resolvedRows"], "qualified references")
    require({c: sum(k[2] == c for k in keys) for c in COLLECTIONS.values()} == expected["counts"], "record counts")
    snapshot = bundle["snapshots"][0]
    presence = {k: "present" if k in snapshot["values"] else "absent" if k in snapshot["absentFields"] else "unknown" for k in FIELDS}
    require(presence == expected["snapshotPresence"], "snapshot presence")
    for name in ("canonicalPayloadHashes", "normalizedObservationIds"):
        require(expected[name] == "pending_independent_RFC8785_oracle", "canonical oracle remains pending")


def edit(bundle, operations):
    for op, path, *value in operations:
        parent = bundle
        for component in path[:-1]:
            parent = parent[component]
        if op == "set":
            parent[path[-1]] = deepcopy(value[0])
        elif op == "delete":
            del parent[path[-1]]
        elif op == "append":
            parent[path[-1]].append(deepcopy(value[0]))
        elif op == "copy":
            original = bundle
            for component in value[0]:
                original = original[component]
            if path[-1] == "-":
                parent.append(deepcopy(original))
            else:
                parent[path[-1]] = deepcopy(original)
        else:
            raise AssertionError("unrecognized finite edit")


def main():
    require(len(sys.argv) == 1, "no arguments supported")
    root = Path(__file__).parent
    # This is the only read site: names are literals above, never fixture values.
    raw = {key: (root / name).read_bytes() for key, name in FILES.items()}
    bundle = {key: [parse(line) for line in data.splitlines()] if FILES[key].endswith(".jsonl") else parse(data) for key, data in raw.items()}
    expected, variants = bundle.pop("expected"), bundle.pop("variants")
    require(not integrity(raw, bundle["manifest"], expected), "raw identities")
    facts(bundle, expected)
    require(len({v["id"] for v in variants}) == len(variants), "duplicate variant IDs")
    for case in variants:
        prefixes = {issue.split(":")[0] for issue in case["issues"]}
        category = next((p for p in ("fatal", "unsupported", "insufficient") if p in prefixes), "valid")
        require(case["outcome"] == category or category == "valid" and case["outcome"] == "valid_unknown", case["id"] + " category")
        changed, changed_raw = deepcopy(bundle), dict(raw)
        edit(changed, case.get("edits", []))
        if case.get("duplicateExport"):
            source = deepcopy(changed["manifest"]["sources"][0])
            source.update(id="updated-copy", path="events-updated-copy.json")
            changed["manifest"]["sources"].append(source)
            mapping = deepcopy(changed["manifest"]["mappings"][0])
            mapping.update(id="map-copy", sourceId="updated-copy")
            changed["manifest"]["mappings"].append(mapping)
            changed["updated-copy"] = deepcopy(changed["updated"])
            changed_raw["updated-copy"] = raw["updated"]
            require(source["sha256"] == hashlib.sha256(changed_raw["updated-copy"]).hexdigest(), "duplicate bytes")
        if case.get("layer") == "raw":
            if "appendBytes" in case:
                changed_raw[case["appendBytes"]] += b" "
            errors = integrity(changed_raw, changed["manifest"], expected)
        else:
            errors, keys, resolved = inspect(changed)
            if "observationCount" in case:
                require(len(keys) == case["observationCount"] and len({tuple(k) for k in keys}) == len(keys), case["id"] + " observations")
            if "resolvedRows" in case:
                require(resolved == case["resolvedRows"], case["id"] + " refs")
        require(sorted(errors) == sorted(case["issues"]), f'{case["id"]}: expected {case["issues"]}, got {sorted(errors)}')
        for assertion in case.get("facts", []):
            source, path, value = assertion
            require(exact(pointer(changed[source], path), value), case["id"] + " value")
    controls = 0
    for source in ("updated", "manifest"):
        altered = dict(raw)
        altered[source] += b" "
        require(bool(integrity(altered, bundle["manifest"], expected)), "undetected raw corruption")
        controls += 1
    wrong = deepcopy(expected)
    wrong["facts"][0]["value"] = "evt_wrong_oracle"
    try:
        facts(bundle, wrong)
    except AssertionError:
        controls += 1
    else:
        raise AssertionError("wrong expected value escaped")
    for data in (b'{"x":1,"x":2}', b'{"x":NaN}'):
        try:
            parse(data)
        except AssertionError:
            controls += 1
        else:
            raise AssertionError("encoding control escaped")
    print(f'PASS: 6 raw sources + manifest identity; {len(expected["facts"])} independent facts; 5 observations; {len(variants)} variants; {controls} additional corruption controls.')


if __name__ == "__main__":
    main()
