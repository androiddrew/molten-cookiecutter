# cookiecutter-molten

A Molten template for [cookiecutter](https://github.com/audreyr/cookiecutter) with a preference for a postgres backend

## Usage

```
$ pip install cookiecutter
$ cookiecutter https://github.com/androiddrew/cookiecutter-molten
```
You will be asked for some basic information regarding your project (name, project name, etc.). This info will be used in your new project

#### Create virtual env
```
$ cd <app_dir>
$ python -m venv env
$ source env/bin/activate
$ pip install -r dev_requirements.txt
$ pip-sync dev_requirements.txt requirements.txt
```
#### Run tests
```
$ pytest -v
```

#### Run dev server
```
$ python manage.py runserver
```

## License

MIT Licensed.

## Changelog

### 0.1.0 (12/09/2018)
- Initial release