CREATE DATABASE IF NOT EXISTS d4ai_devdb;
CREATE USER IF NOT EXISTS 'd4ai_devdb_user'@'%' IDENTIFIED BY 'd4ai_devdb_pwd';
GRANT ALL PRIVILEGES ON d4ai_devdb.* TO 'd4ai_devdb_user'@'%';
FLUSH PRIVILEGES;
