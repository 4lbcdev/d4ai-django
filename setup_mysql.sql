-- Description: This script is used to setup the MySQL database for the D4AI project.
DROP DATABASE IF EXISTS d4ai_db;
CREATE DATABASE IF NOT EXISTS d4ai_db;
CREATE USER IF NOT EXISTS 'd4ai_db_user'@`localhost` IDENTIFIED BY 'd4ai_db_pwd';
GRANT ALL PRIVILEGES ON d4ai_db.* TO 'd4ai_db_user'@'localhost';
FLUSH PRIVILEGES;