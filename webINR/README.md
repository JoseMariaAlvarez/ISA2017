# Web INR

Working on a venv is recommended.
```
$ virtualenv inr
$ source bin/activate
```
Once on a virtualenv, clone the repository and install the given requirements.
```
$ pip install -r requirements.txt
```
Once done, firstly we'll need a superuser.
```
$ python manage.py createsuperuser
```
And afterwards migrate the project
```
$ python manage.py makemigrations
```
To run the server simply:
```
$ python manage.py runserver 
```
