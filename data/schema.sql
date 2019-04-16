<--DB script-->

CREATE DATABASE emex;

USE emex;

CREATE TABLE reportes (
    id_reporte int primary key auto_increment,
    nombre varchar(100) NOT NULL,
    edad int (3) NOT NULL,
    latitud varchar(100) NOT NULL,
    longitud varchar(100) NOT NULL
);

CREATE USER 'chay'@'localhost' IDENTIFIED BY 'chay';
GRANT ALL PRIVILEGES ON emex.* TO 'chay'@'localhost';
FLUSH PRIVILEGES;