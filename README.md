## dev setup
clone repo and create virtual env
```bash
cd <project-dir>
git clone https://github.com/joshcannella/osrs-gept.git
python3 -m venv .venv
```
activate the virtual env (Windows):
```bash
.venv\scripts\activate
```
activate the virtual env (Mac OS):
```bash
. .venv/bin/activate
```
## setuptools integration
to test the script, make a new virtual env and then install the package:
```bash
python3 -m venv .venv
. .venv/bin/activate
pip install --editable .
```
run the command
```bash
gept --help
```