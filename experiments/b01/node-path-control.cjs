// Deliberately unsafe negative control: O_NOFOLLOW alone does not protect ancestors.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const scratch = '/Volumes/AIWorkspace/caches/hooktrace/b01';
fs.mkdirSync(scratch, { recursive: true });
const base = fs.mkdtempSync(path.join(scratch, 'node-control-'));
const flags = fs.constants.O_RDONLY | fs.constants.O_NOFOLLOW;
function readLeaf(file) {
  const fd = fs.openSync(file, flags);
  try {
    assert.ok(fs.fstatSync(fd).isFile());
    return fs.readFileSync(fd, 'utf8');
  } finally {
    fs.closeSync(fd);
    assert.throws(() => fs.fstatSync(fd), { code: 'EBADF' });
  }
}
try {
  const input = path.join(base, 'input');
  const outside = path.join(base, 'outside');
  fs.mkdirSync(input);
  fs.mkdirSync(outside);
  fs.writeFileSync(path.join(input, 'leaf'), 'original');
  fs.writeFileSync(path.join(outside, 'leaf'), 'outside-sentinel');
  assert.equal(readLeaf(path.join(input, 'leaf')), 'original');
  fs.renameSync(input, `${input}.original`);
  fs.symlinkSync(outside, input);
  assert.equal(readLeaf(path.join(input, 'leaf')), 'outside-sentinel');
  fs.symlinkSync(path.join(outside, 'leaf'), path.join(base, 'leaf-link'));
  assert.throws(() => readLeaf(path.join(base, 'leaf-link')), { code: 'ELOOP' });
  console.log(JSON.stringify({ node: process.version, openat: typeof fs.openat,
    positive: 'original', ancestorSubstitution: 'outside-sentinel',
    leafSymlink: 'ELOOP', descriptors: 'closed', verdict: 'path-only mechanism NO-GO' }));
} finally {
  fs.rmSync(base, { recursive: true });
}
