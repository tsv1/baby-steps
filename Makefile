.PHONY: build
build:
	pip3 install --quiet --upgrade pip
	pip3 install --quiet --upgrade setuptools wheel twine
	python3 setup.py sdist bdist_wheel

.PHONY: publish
publish:
	twine upload dist/*

.PHONY: test
test:
	python3 -m unittest discover .

.PHONY: bump
bump:
	bump2version $(filter-out $@,$(MAKECMDGOALS))
	@git --no-pager show HEAD
	@echo
	@git verify-commit HEAD
	@git verify-tag `git describe`
	@echo
	# git push origin master --tags
%:
	@:
