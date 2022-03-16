CREATE TABLE `Products` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`ingredients` varchar(255) NOT NULL,
	`description` varchar(255) NOT NULL,
	`price` INT NOT NULL,
	`available` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Orders` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`id_p` INT NOT NULL,
	`status` varchar(255) NOT NULL,
	`id_e` INT(255) NOT NULL,
	`id_c` INT(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Customer` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Employee` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`phone_number` varchar(255) NOT NULL,
	`address` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `Orders` ADD CONSTRAINT `Orders_fk0` FOREIGN KEY (`id_p`) REFERENCES `Products`(`id`);

ALTER TABLE `Orders` ADD CONSTRAINT `Orders_fk1` FOREIGN KEY (`id_e`) REFERENCES `Employee`(`id`);

ALTER TABLE `Orders` ADD CONSTRAINT `Orders_fk2` FOREIGN KEY (`id_c`) REFERENCES `Customer`(`id`);





