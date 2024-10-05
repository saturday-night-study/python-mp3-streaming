```bash
source .venv/bin/activate

pip install coverage

coverage run -m unittest discover
coverage report -m
```