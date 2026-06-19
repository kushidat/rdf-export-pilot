.PHONY: help convert lint ci

help:
@echo "Targets:"
@echo "  make convert  - run RDF conversion"
@echo "  make ci       - run local CI steps"

convert:
python3 scripts/convert_nt.py --input data/sample.nt --outdir output

ci: convert
@echo "CI local check done"
