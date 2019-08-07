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

## Forms Integration
To integrate the forms into the front-end:
Firstly, you need to make the user access token which you obtain from the authentication stage
 accessible for the forms to use by setting variable `WORKFLOW_TOKEN` to the document window. 
 Something like `window.WORKFLOW_TOKEN = 'c3e0ed87dec308e20f32bcce63185f0940810a2a'`
The whole form process doesn't really involve the frontend designer so much, you are just 
required to handle end events of processes such as (form creation, form submission ...).
Remember to user full URLs when hitting the endpoints as you follow the guide.

### The admin/organization handler side
#### Creating a form
- On the page where you intend to create the form in the front end, create an `<iframe>` element wherever 
on the page you want the form builder to appear.
For example, I created this:
```html
<iframe src="" id="form-builder" frameborder="0" style="min-height: 600px; overflow: auto; width: 100%;"></iframe>
```
- Send a `GET` ajax request to endpoint `/process/formbuilder/org/<organization_id>/create/` (Fill in <organization_id> with 
the organization this form would be created under), response type is `HTML`, fill in the response into the `iframe` you created 
earlier. For example:
```js
$.ajax({
    url: "/process/formbuilder/org/1/create/", // 1 is my organization_id
    headers: {"Authorization": "Token " + window.WORKFLOW_TOKEN},
    success: function (response) {
        $('#form-builder').attr('srcdoc', response)
    }
});
```

#### Communicating with the iframe
- At this point, the form builder should be visible on the page already. When the admin finishes constructing the form as required
and clicks on SAVE, an event is triggered from the formbuilder which might be needed on the frontend, maybe to navigate to another 
page. Event name `workflow-form-saved`. To handle this event, we use the regular iframe communication mechanism. 
In case you need some data here from what is going on in the iframe, you can access data returned from the server through the `detail`
attribute of the event. Sample below:
```js
window.document.addEventListener('workflow-form-saved', function (e) {
    // Your code would go in here, and to access data sent, just do 'e.detail'
}, false)
```

#### Updating a form
- If you also wish to update the form built, you can go through the similar process and retrieve the html code from 
`/process/formbuilder/org/<organization_id>/view/<form_id>/` and slot the response into an iframe. Sample code:
```js
$.ajax({
    url: "/process/formbuilder/org/1/update/15/", // 1 is the organization_id and 15 is the form_id I wish to update
    headers: {"Authorization": "Token " + window.WORKFLOW_TOKEN},
    success: function (response) {
        $('#form-builder').attr('srcdoc', response) // form-builder is the id of the iframe we are using
    }
});
``` 
Same thing also goes here, an event is triggered from the iframe which you can handle on the outdie using the sample initally stated.

#### Rendering the form for the end-user
- Lastly, on the user end, when the user needs to fill the form, there's only one endpoint you need to hit in this case,
since a user can fill a form only once, if eventually the frontend permits them to comeback to it, they'd only be updating the previous 
data as form would be prepopulated with their data. End point is `/process/formbuilder/org/<organization_id>/view/<form_id>/`
Sample code:
```js
$.ajax({
    url: "/process/formbuilder/org/1/view/15/", // 1 is the organization_id and 15 is the form_id I wish to update
    headers: {"Authorization": "Token " + window.WORKFLOW_TOKEN},
    success: function (response) {
        $('#form-builder-render').attr('srcdoc', response) // form-builder-render is the id of the iframe we are using
    }
});
```
Event emitted by this action, (when the user submits the form) is `'user-submitted-workflow-form'`. So you might be able to handle 
this event with.
```js
window.document.addEventListener('user-submitted-workflow-form', function (e) {
    // Your code would go in here, and to access data sent, just do 'e.detail'
}, false)
```

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
