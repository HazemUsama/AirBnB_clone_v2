-- Setup the database for development
CREATE DATABASE IF NOT EXIIST `hbnb_dev_db`
CREATE USER IF NOT EXISTS `hbnb_dev`@`localhost` IDENTIFIED BY 'hbnb_dev_pwd'
GRANT ALL PRIVILEGE ON `hbnb_dev_db`.* TO  `hbnb_dev`@`localhost`
GRANT SELECT ON `performance_schema`.* TO `hbnb_dev`@`localhost`;
