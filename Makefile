.SILENT: run install venv test test-watch format clean

all: install run

install: venv
		. .venv/bin/activate && pip install --disable-pip-version-check -r requirements.txt

venv:
		test -d v.env || python3 -m venv .venv

run:
		. .venv/bin/activate && pip -V

test: install
		. .venv/bin/activate && pytest

test-watch: install
		. .venv/bin/activate && ptw .

format: install
		. .venv/bin/activate && black .

clean:
		rm -rf .venv
		find -iname "*.pyc" -delete