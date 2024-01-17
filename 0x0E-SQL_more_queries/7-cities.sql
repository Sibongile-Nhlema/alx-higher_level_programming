-- This script creats the database , hbtn_0d_usa
-- And the table, cities with the following descriptions
-- id, state_id and name
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	`id` INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	`state_id` INT NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	FOREIGN KEY (`state_id`) REFERENCES states(`id`));

