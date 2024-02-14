-- 5-unique_id.sql

-- This a script that creates the table unique_id on your MySQL server
CREATE TABLE IF NOT EXISTS unique_id (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256),
	PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
