--we are all unique
--creating a table with constraints
CREATE TABLE IF NOT EXISTS users(
	COMMENT="CREATING A TABLE",
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255));
