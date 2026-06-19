import csv
import json
import argparse
from pathlib import Path

def parse_args():
    p = argparse.ArgumentParser(description="Convert N-Triples (.nt) to CSV/TSV/JSON")
    p.add_argument("--input", "-i", default="data/sample.nt", help="Input .nt file path")
    p.add_argument("--outdir", "-o", default="output", help="Output directory")
    return p.parse_args()

def main():
    args = parse_args()
    inp = Path(args.input)
    out_dir = Path(args.outdir)

    if not inp.exists():
        raise FileNotFoundError(f"Input file not found: {inp}")

    out_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    for line in inp.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or not line.endswith(" ."):
            continue

        body = line[:-2].strip()
        parts = body.split(" ", 2)
        if len(parts) != 3:
            continue

        s, p, o = parts
        rows.append({"subject": s, "predicate": p, "object": o})

    # CSV
    with (out_dir / "triples.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["subject", "predicate", "object"])
        w.writeheader()
        w.writerows(rows)

    # TSV
    with (out_dir / "triples.tsv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["subject", "predicate", "object"], delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    # JSON
    (out_dir / "triples.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"Wrote {len(rows)} triples to {out_dir}/ (csv, tsv, json)")

if __name__ == "__main__":
    main()
