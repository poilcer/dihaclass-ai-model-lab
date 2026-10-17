from pathlib import Path
import hashlib,json,zipfile
root=Path(__file__).parent
manifest=json.loads((root/'PUBLIC_MANIFEST.json').read_text(encoding='utf-8'))
for name,digest in manifest.items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
expected=['shorts.md','factcheck.csv','costs.csv','demo.html']
files=[root/m/n for m in ['argon','sol','opus'] for n in expected]
assert len(files)==12 and all(f.is_file() for f in files)
with zipfile.ZipFile(root/'Model_Examples.zip') as z:
    assert z.testzip() is None
    for p in files:assert z.read(str(p.relative_to(root)).replace('\\','/'))==p.read_bytes()
print('PASS: public manifest hashes, 12 original outputs and ZIP byte identity')
