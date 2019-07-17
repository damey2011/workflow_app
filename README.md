<h1 align="center">Welcome to Workflow801 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/damey2011/workflow_app">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" target="_blank" />
  </a>
</p>

> Backend/API service for a simple workflow automation software

## Install

```sh
pip install -r requirements.txt
```

## Usage

```sh
python manage.py runserver
```
This uses the default settings in the `settings.py` file, but in other to use
custom settings e.g. different database user or database name, then duplicate the 
`settings.ini` file and name it `settings.dev.ini` and put in your own values here.
The reason for duplicating is that, `settings.dev.ini` is ignored by git so it 
doesn't affect the other developer. This way we can keep different custom 
non-application-dependent settings.

## Extra

If there is a need to export the database on the remote server to use on development machine, 
we can reach 
```bash
https://sitename.com/utility/db-export/
```
Understood that this may be a security risk, so it's going to be available only in 
development mode i.e. when `DEBUG=True` in settings.

## Author

👤 **Python Group CSC 801**


## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/damey2011/workflow_app/issues).

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_