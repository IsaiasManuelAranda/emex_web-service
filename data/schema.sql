CREATE TABLE `usuario` (
	`email_user` VARCHAR(30) NOT NULL,
	PRIMARY KEY (`email_user`)
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
;


CREATE TABLE `persona_extra` (
	`id_persona` INT(11) NOT NULL AUTO_INCREMENT,
	`nombre_persona` VARCHAR(40) NOT NULL,
	`ape_pat_persona` VARCHAR(40) NOT NULL,
	`ape_mat_persona` VARCHAR(40) NOT NULL,
	`edad` VARCHAR(3) NOT NULL,
	`fecha_extravio` VARCHAR(10) NOT NULL,
	`curp_persona` VARCHAR(18) NOT NULL,
	`sexo` VARCHAR(10) NOT NULL,
	`email_user` VARCHAR(30) NOT NULL,
	PRIMARY KEY (`id_persona`),
	INDEX `email_user` (`email_user`),
	CONSTRAINT `persona_extra_ibfk_1` FOREIGN KEY (`email_user`) REFERENCES `usuario` (`email_user`)
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
AUTO_INCREMENT=6
;
