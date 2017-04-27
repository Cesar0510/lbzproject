
env = env/bin
python = $(env)/python
pip = $(env)/pip


server:
		$(python) manage.py runserver

clean:
		find . -path ./env -prune -o -type d -name '__pycache__' -exec rm -rf {} \;

install:
		python3 -m venv env
		$(pip) install -r requirements/local.txt

shell:
		$(python) manage.py shell

