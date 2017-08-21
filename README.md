Clinical Scores
===============

## Python 2.7 virtual environment

Created with:

```bash
conda create -n env python=2.7
pip install flask selenium flask_script flask_bootstrap flask_sqlalchemy
```

To activate this environment, use:
```bash
source activate venv
```

To deactivate an active environment, use:
```bash
> source deactivate
```

## Python 3.6.1 virtual environment

Created with:
```bash
mkvirtualenv --python=python3.6 clinicalscores
pip install flask selenium flask_script flask_bootstrap

```

To activate this environment, use:
```bash
> workon clinicalscores
```

To deactivate an active environment, use:
```bash
> source deactivate
```

## To Run the app
To Run the server:
```bash
python clinicalscores.py runserver
```

## Testing
To run tests:
```bash
python functional_tests.py
```

## about me 
THis is an web app!
