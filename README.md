# rdf-export-pilot

RDF N-Triples (`.nt`) を **CSV / TSV / JSON** に変換する最小プロジェクトです。

## 構成

- `data/sample.nt` : サンプルRDFデータ（N-Triples）
- `scripts/convert_nt.py` : 変換スクリプト
- `output/` : 生成物（`.gitignore` で除外）
- `.github/workflows/convert.yml` : `main` push時に自動実行

## 必要環境

- Python 3.10+（推奨: 3.11）

## 使い方

```bash
python3 scripts/convert_nt.py
ls -1 output
```

生成されるファイル:

- `output/triples.csv`
- `output/triples.tsv`
- `output/triples.json`

## CI（GitHub Actions）

`main` ブランチへの push、または手動実行で次を実行します。

```bash
python scripts/convert_nt.py
```

GitHub の **Actions** タブで **Convert RDF sample** を確認できます。

## ライセンス

MIT（必要に応じて変更してください）

- `output/predicate_counts.csv`（predicateごとの件数）
