# define the name of the virtual environment directory
VENV := venv

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate: requirements.txt
	virtualenv -p python3 $(VENV)
	. $(PWD)/$(VENV)/bin/activate
	./$(VENV)/bin/pip3 install -r requirements.txt
	touch caminhada
	echo "#!/bin/sh" >> caminhada
	echo ". venv/bin/activate" >> caminhada
	echo "python3 ./main.py" >> caminhada
	chmod +x $(PWD)/main.py
	chmod +x $(PWD)/caminhada

# venv is a shortcut target
venv: $(VENV)/bin/activate

clean:
	rm -rf $(VENV)
	rm caminhada
	find . -type f -name '*.pyc' -delete

.PHONY: all venv clean