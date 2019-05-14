# cookiecutter-molten

A Molten template for [cookiecutter](https://github.com/audreyr/cookiecutter) with a preference for a postgres backend

## Usage

```
$ pip install cookiecutter
$ cookiecutter https://github.com/androiddrew/molten-cookiecutter
```
You will be asked for some basic information regarding your project (name, project name, etc.). This info will be used in your new project

#### Create a virtual environment
```
$ cd <app_dir>
$ python -m venv env
$ source env/bin/activate
```

Follow the initial setup steps included in the project.

#### Run tests
```
$ env ENVIRONMENT=test pytest -v
```

#### Using the management script
In a similar style to Django this cookiecutter provides a `manage.py` module to assist you in your development. This script is simply assembled using the [click](https://github.com/pallets/click) library. 

Excuting the script with no parameters will print a list of available operations.
```
$ python manage.py
```



If you have installed the dev dependencies you will have access to the werkzueg dev server. Do not use this server in production.
```
$ python manage.py runserver
```

## License

MIT Licensed.

## Changelog

### 0.3.1 (02/08/2019)
- Fixed failure in license selection.

### 0.3.0 (01/27/2019)
- Added migrations.
- Changed testing fixtures.

### 0.2.0 (01/15/2019)
- Added TOML settings file and .coveragerc file.

### 0.1.0 (12/09/2018)
- Initial release.
