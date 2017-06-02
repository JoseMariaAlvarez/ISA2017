INSERT INTO INR_medicacion(nombre) VALUES ('Sintrom 1mg');
INSERT INTO INR_medicacion(nombre) VALUES ('Sintrom 4mg');

INSERT INTO INR_comentario(text) VALUES ('El paciente se encuentra bien');
INSERT INTO INR_comentario(text) VALUES ('El paciente necesita atencion');

INSERT INTO INR_pacienteclinica (NSS,DNI,Nombre,Apellido_1,Apellido_2,Direccion,CP,Telefono,Ciudad,Provincia,Pais,password, Fecha_nacimiento,Sexo, token, rango) VALUES (258465745,'57489634Y','Rocio','Murillos','Ortiz','C/Salzillo',29008,648584898,'Malaga','Malaga','Spain','perro','1945/1/23','Mujer', '2d2d2', '1-2');
INSERT INTO INR_pacienteclinica (NSS,DNI,Nombre,Apellido_1,Apellido_2,Direccion,CP,Telefono,Ciudad,Provincia,Pais,password,Fecha_nacimiento,Sexo, token, rango) VALUES (54789214,'25654498E','Miguel','Garcia','Toro','C/Alfarnate',29558,635241859,'Malaga','Malaga','Spain','gato','1934/3/21','Hombre', 'wdwd', '1-3');
INSERT INTO INR_pacienteclinica (NSS,DNI,Nombre,Apellido_1,Apellido_2,Direccion,CP,Telefono,Ciudad,Provincia,Pais,password,Fecha_nacimiento,Sexo, token, rango) VALUES (98762583,'98954787A','Alberto','Casas','Diaz','C/Sol',15845,695847596,'Malaga','Malaga','Spain','vaca','1955/5/6','Hombre', 'efere', '2-3');
INSERT INTO INR_pacienteclinica (NSS,DNI,Nombre,Apellido_1,Apellido_2,Direccion,CP,Telefono,Ciudad,Provincia,Pais,password,Fecha_nacimiento,Sexo, token, rango) VALUES (369214782,'18428549F','Daniel','Puertas','Seguras','C/Larios',84985,695812036,'Malaga','Malaga','toro','Spain','1945/7/12','Hombre', '3r3r3', '2-3');

INSERT INTO INR_diagnostico(idDiagnostico, nombre, paciente_id) VALUES ('11223T', 'Rocio Murillos Ortiz', '258465745');
INSERT INTO INR_diagnostico(idDiagnostico, nombre, paciente_id) VALUES ('13434R', 'Miguel Garcia Toro', '54789214');
INSERT INTO INR_diagnostico(idDiagnostico, nombre, paciente_id) VALUES ('25887D', 'Alberto Casas Diaz', '98762583');
INSERT INTO INR_diagnostico(idDiagnostico, nombre, paciente_id) VALUES ('98975K', 'Daniel Puertas Seguras', '369214782');

INSERT INTO INR_visita(fecha, valorINR, dosis, duracion, peso, paciente_id, comentario_id, medicacion_id) VALUES ('2016/10/22', 2.1, 100, '1 Semana', 84.5, 9, 1, 1 );
INSERT INTO INR_visita(fecha, valorINR, dosis, duracion, peso, paciente_id, comentario_id, medicacion_id) VALUES ('2016/12/31', 2.7, 80, '2 Semanas', 84.5, 10, 2, 2 );
