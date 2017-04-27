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

Also, we need to create the *login* database:
```SQL
CREATE DATABASE usuariossanitarios;
USE usuariossanitarios;

CREATE TABLE `usuarios_sanitarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(8) NOT NULL UNIQUE,
  `password` varchar(8) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `apellido1` varchar(25) NOT NULL,
  `apellido2` varchar(25) DEFAULT NULL,
  `categoria` varchar(50) NOT NULL,
  `centro` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `usuarios_sanitarios`(nombre,apellido1,apellido2,categoria,centro,usuario,password)
VALUES("Marco","Polo","de Venecia","Médico","Hp.H","test","test1");
```

### Install using Anaconda

To install simply (for `MySQLdb`):
```
$ conda install mysql-python
```

Or (for `mysql.connector`):
```
$ conda install -c anaconda mysql-connector-python=2.0.4
```
