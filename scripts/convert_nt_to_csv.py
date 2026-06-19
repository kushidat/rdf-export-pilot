import csv
from pathlib import Path

inp = Path("data/sample.nt")
out = Path("output/triples.csv")
out.parent.mkdir(parents=True, exist_ok=True)

rows = []
for line in inp.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    if not line.endswith(" ."):
        continue
    body = line[:-2].strip()
    parts = body.split(" ", 2)
    if len(parts) != 3:
        continue
    s, p, o = parts
    rows.append((s, p, o))

with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["subject", "predicate", "object"])
    w.writerows(rows)

print(f"Wrote {len(rows)} triples to {out}")
