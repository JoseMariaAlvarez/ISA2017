# Web INR

Working on a venv is recommended.
```
$ virtualenv inr
$ source bin/activate
```
Once on a virtualenv, clone the repository and install the given requirements.
```
$ pip install --proxy <proxyHost>:<proxyPort> -r requirements.txt
```
Once done, firstly we'll need a superuser.
```
$ python manage.py createsuperuser
```
And afterwards migrate the project
```
$ python manage.py migrate
$ python manage.py makemigrations
```
To run the server simply:
```
$ python manage.py runserver
```

### Install Django using Anaconda

To create a new environment,
```
$ conda create --name django python=2.7
```
Clone the repository,
```
$ git clone https://github.com/JoseMariaAlvarez/ISA2017.git
```
Activate the environment,
```
$ activate django
```
Install the requirements,
```
$ pip install --proxy <proxyHost>:<proxyPort> -r requirements.txt
```

# Working with MySQL

For local testing purposes, MySQL-Python will be required.

```
$ sudo apt install libmysqlclient-dev
$ pip install MySQL-python
```
