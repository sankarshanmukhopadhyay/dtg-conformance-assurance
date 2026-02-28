PYTHON?=python

.PHONY: validate export-risk coverage

validate:
	$(PYTHON) tools/validate.py

export-risk:
	$(PYTHON) tools/export_xlsx_to_csv.py

coverage:
	SOURCE_DATE_EPOCH=0 $(PYTHON) tools/coverage_report.py --bundle templates/starter-bundle --out risk/reports/coverage
