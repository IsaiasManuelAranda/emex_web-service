create database emex;

use emex;

create table usuario(
    id_user int primary key not null auto_increment,
    nombre_user varchar(30) not null,
    ape_pat_user varchar(30) not null,
    ape_mat_user varchar(30) not null,
    telefono_user varchar(10) not null,
    email_user varchar(30) not null,
    passwd varchar(20) not null
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table persona_extra(
    id_persona int primary key auto_increment,
    nombre_persona varchar(40) not null,
    ape_pat_persona varchar(40) not null,
    ape_mat_persona varchar(40) not null,
    edad varchar(3) not null,
    fecha_extravio date not null,
    curp_persona varchar(18) not null,
    sexo varchar(10) not null,
    id_user int not null
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE persona_extra add FOREIGN KEY(id_user) REFERENCES usuario(id_user);

CREATE USER 'chay'@'localhost' IDENTIFIED BY 'chay';
GRANT ALL PRIVILEGES ON emex.* TO 'chay'@'localhost';
FLUSH PRIVILEGES;

insert into usuario (id_user, nombre_user, ape_pat_user, ape_mat_user, telefono_user, email_user, passwd) values
(1, 'Pedro',    'Sanchez',  'Martinez', '7751623483', 'pedroSM@gmail.com',      'pedrin'),
(2, 'Juan',     'Lopez',    'Juarico',  '7823716234', 'juanito@gmail.com',      'juan'),
(3, 'Fernando', 'Origel',   'Cuaron',   '7726155263', 'fernandin@gmail.com',    'fernandote');

insert into persona_extra(id_persona, nombre_persona, ape_pat_persona, ape_mat_persona, edad, fecha_extravio, curp_persona, sexo, id_user) values
(1, 'Arturo',   'Jimenez',  'Badillo',  '20',   '2019-03-19',   'ASDERT24562FDS43TR', 'masculino',  2),
(2, 'Gabriela', 'Curiel',   'Garcia',   '19',   '2014-10-14',   'QWASFD12524SFDS53G', 'femenino',   2),
(3, 'Lucas',    'Gomez',    'Arana',    '35',   '2016-10-16',   'AQWZXCFG3827345CVG', 'masculino',  1);

select usuario.nombre_user, persona_extra.nombre_persona from persona_extra inner join usuario on persona_extra.id_user = usuario.id_user;
select usuario.nombre_user, persona_extra.nombre_persona from persona_extra inner join usuario on persona_extra.id_user = usuario.id_user where nombre_user='Pedro';
select usuario.nombre_user, persona_extra.nombre_persona from persona_extra inner join usuario on persona_extra.id_user = usuario.id_user where nombre_user='Juan';
select usuario.nombre_user, persona_extra.nombre_persona from persona_extra inner join usuario on persona_extra.id_user = usuario.id_user where nombre_user='Fernando';

