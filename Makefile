lint:
	flake8 --ignore=E402,E501,E712,W503,E203,I002 --exclude=ctfcli/templates **/*.py
	black --check --exclude=ctfcli/templates .

format:
	black --exclude=ctfcli/templates .

install:
	python3 setup.py install

build:
	python3 setup.py sdist bdist_wheel

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf ctfcli.egg-info/
