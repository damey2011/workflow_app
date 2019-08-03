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
This uses the default settings in the `settings.py` file, but in order to use
custom settings e.g. different database user or database name, then duplicate the 
`settings.dev.ini` file and name it `settings.ini` and put in your own values here.
The reason for duplicating is that, `settings.ini` is ignored by git so it 
doesn't affect the other developer. This way we can keep different custom 
non-application-dependent settings.   

### Sign up - Endpoint: https://workflow801.herokuapp.com/account/signup  
Sample request:
```sh
{"email":"demouser@gmail.com","password":"demouser","first_name":"Demo","last_name":"User"}
```
Sample Response:
```sh
{
    "Token": "b9bf9516f1b62d625273b803f37df6c462aef43f",
    "Expires_in": "86399.984865",
    "User": {
        "id": 2,
        "first_name": "Demo",
        "last_name": "User",
        "email": "demouser@gmail.com",
        "date_of_birth": null,
        "address": null,
        "state": null,
        "gender": null,
        "phone_number": "",
        "profile_pic": null,
        "createdorgs": [],
        "createdgroups": [],
        "userorganizations": [],
        "usergroups": [],
        "createdprocesses": [],
        "createdstage": [],
        "createdtask": [],
        "userforms": [],
        "userdocuments": [],
        "tasks_to_user": [],
        "userformresponse": []
    }
}
```  
### Login - Endpoint: https://workflow801.herokuapp.com/account/login 
Sample request:
```sh
{"email":"demouser@gmail.com","password":"demouser"}
```
Sample response:
```sh
{
    "Token": "b9bf9516f1b62d625273b803f37df6c462aef43f",
    "Expires_in": "86399.984865",
    "User": {
        "id": 2,
        "first_name": "Demo",
        "last_name": "User",
        "email": "demouser@gmail.com",
        "date_of_birth": null,
        "address": null,
        "state": null,
        "gender": null,
        "phone_number": "",
        "profile_pic": null,
        "createdorgs": [],
        "createdgroups": [],
        "userorganizations": [],
        "usergroups": [],
        "createdprocesses": [],
        "createdstage": [],
        "createdtask": [],
        "userforms": [],
        "userdocuments": [],
        "tasks_to_user": [],
        "userformresponse": []
    }
}  
```
### Authentication  
We are using a (modified) Django rest-framework in-built token authentication (similar to JWT). After a login or signup, you must include the authentication token in your request header like this;  
```sh
{  
 Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b  
}  
```
Take not of the "Token" keyword before the actual token, it must be included exactly the same way, else Django rest-framework won't acknowledge it. When a token has expired, the user will need to login in again and a refreshed token will be issued. Token lifespan is 24 hours.  

View the full Schema of the application at;
https://workflow801.herokuapp.com/schema  

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
