PYTHON?=python

.PHONY: validate test export-risk coverage

validate: test
	$(PYTHON) tools/validate.py

test:
	$(PYTHON) -m unittest discover -s tests -p 'test_*.py'

export-risk:
	$(PYTHON) tools/export_xlsx_to_csv.py

coverage:
	SOURCE_DATE_EPOCH=0 $(PYTHON) tools/coverage_report.py --bundle templates/starter-bundle --out risk/reports/coverage
