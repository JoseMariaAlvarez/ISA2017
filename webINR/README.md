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

Also, we need to create the *login* and *patients* database:
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

```SQL
CREATE TABLE `pacientes` (
  `NSS` int(11) NOT NULL,
  `DNI` varchar(15) NOT NULL,
  `Nombre` varchar(25) NOT NULL,
  `Apellido1` varchar(25) NOT NULL,
  `Apellido2` varchar(25) NOT NULL,
  `Direccion` varchar(45) DEFAULT NULL,
  `CP` int(11) NOT NULL,
  `Telefono` varchar(11) DEFAULT NULL,
  `Ciudad` varchar(45) NOT NULL,
  `Provincia` varchar(45) NOT NULL,
  `Pais` varchar(45) NOT NULL,
  `Fecha_Nacimiento` date NOT NULL,
  `Sexo` varchar(15) NOT NULL,
  PRIMARY KEY (`NSS`)
);

INSERT INTO paciente (NSS,DNI,Nombre,Apellido1,Apellido2,Direccion,CP,Telefono,Ciudad,Provincia,Pais,Fecha_nacimiento,Sexo) VALUES (258465745,'57489634Y','Rocio','Murillos','Ortiz','C/Salzillo',29008,648584898,'Malaga','Malaga','Spain','1945/1/23','Mujer');
INSERT INTO paciente (NSS,DNI,Nombre,Apellido1,Apellido2,Direccion,CP,Telefono,Ciudad,Provincia,Pais,Fecha_nacimiento,Sexo) VALUES (54789214,'25654498E','Miguel','Garcia','Toro','C/Alfarnate',29558,635241859,'Malaga','Malaga','Spain','1934/3/21','Hombre');
INSERT INTO paciente (NSS,DNI,Nombre,Apellido1,Apellido2,Direccion,CP,Telefono,Ciudad,Provincia,Pais,Fecha_nacimiento,Sexo) VALUES (98762583,'98954787A','Alberto','Casas','Diaz','C/Sol',15845,695847596,'Malaga','Malaga','Spain','1955/5/6','Hombre');
INSERT INTO paciente (NSS,DNI,Nombre,Apellido1,Apellido2,Direccion,CP,Telefono,Ciudad,Provincia,Pais,Fecha_nacimiento,Sexo) VALUES (369214782,'18428549F','Daniel','Puertas','Seguras','C/Larios',84985,695812036,'Malaga','Malaga','Spain','1945/7/12','Hombre');
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
