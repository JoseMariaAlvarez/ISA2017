INSERT INTO INR_medicacion(nombre) VALUES ('Sintrom 1mg');
INSERT INTO INR_medicacion(nombre) VALUES ('Sintrom 4mg');

INSERT INTO INR_pacienteclinica (NSS,DNI,Nombre,Apellido_1,Apellido_2,Direccion,CP,Telefono,Ciudad,Provincia,Pais,password, Fecha_nacimiento,Sexo, token, rango_inf, rango_sup) VALUES (258465745,'57489634Y','Rocio','Murillos','Ortiz','C/Salzillo',29008,648584898,'Malaga','Malaga','Spain','perro','1945/1/23','Mujer', '2d2d2', '1', '2');
INSERT INTO INR_pacienteclinica (NSS,DNI,Nombre,Apellido_1,Apellido_2,Direccion,CP,Telefono,Ciudad,Provincia,Pais,password,Fecha_nacimiento,Sexo, token, rango_inf, rango_sup) VALUES (54789214,'25654498E','Miguel','Garcia','Toro','C/Alfarnate',29558,635241859,'Malaga','Malaga','Spain','gato','1934/3/21','Hombre', 'wdwd', '1','3');

INSERT INTO INR_diagnostico(codigo, descripcion) VALUES ('487', 'Gripe');
INSERT INTO INR_diagnostico(codigo, descripcion) VALUES ('802.1 ', 'Fractira de huesos nariz abierta');
INSERT INTO INR_diagnostico(codigo, descripcion) VALUES ('874', 'Herida abierta cuello');
INSERT INTO INR_diagnostico(codigo, descripcion) VALUES ('835', 'Luxación de cadera');

INSERT INTO INR_medicacion_adicional(nombre) VALUES ('Ibuprofeno 1g');
INSERT INTO INR_medicacion_adicional(nombre) VALUES ('Gelocatil 1g');

INSERT INTO INR_visita(fecha, valorINR, dosis, duracion, peso, paciente_id, medicacion_id) VALUES ('2016/10/22', 2.1, 100, '1', 84.5, 1, 1 );
INSERT INTO INR_visita(fecha, valorINR, dosis, duracion, peso, paciente_id, medicacion_id) VALUES ('2016/12/31', 2.7, 80, '2', 84.5, 2, 2 );

INSERT INTO INR_comentario(text,visita_id,autor) VALUES ('El paciente se encuentra bien',1,'Allie Lewis');
INSERT INTO INR_comentario(text,visita_id,autor) VALUES ('El paciente necesita atencion',1,'Allie Lewis');

