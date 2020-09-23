PACKAGE=hashtag_observer
REQUIREMENTS=requirements.txt

help:
	@echo "Options: make <clean/install/develop/uninstall>"

clean:
	@rm -vrf ./build ./dist ./*.egg-info ./*.egg ./.eggs ./.pytest_cache ./pip-wheel-metadata
	@find . -name '*.pyc' -delete
	@find . -name '*.so' -delete
	@find . -name '__pycache__' -type d -delete

install:
	@pip install -r $(REQUIREMENTS)
	@pip install .

develop:
	@pip install -r $(REQUIREMENTS)
	@pip install -e .

uninstall:
	@pip uninstall $(PACKAGE) -y
