PYTHON?=python

.PHONY: validate export-risk

validate:
	$(PYTHON) tools/validate.py

export-risk:
	$(PYTHON) tools/export_xlsx_to_csv.py
