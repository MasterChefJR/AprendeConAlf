CREATE DATABASE mydb;
USE mydb;
CREATE TABLE mitabla ( id INT PRIMARY KEY, nombre VARCHAR(20) );
INSERT INTO mitabla VALUES ( 1, 'Will' );
INSERT INTO mitabla VALUES ( 2, 'Marry' );
INSERT INTO mitabla VALUES ( 3, 'Dean' );
SELECT id, nombre FROM mitabla WHERE id = 1;
UPDATE mitabla SET nombre = 'Willy' WHERE id = 1;
SELECT id, nombre FROM mitabla;
DELETE FROM mitabla WHERE id = 1;
SELECT id, nombre FROM mitabla;
DROP DATABASE mydb;
SELECT count(1) from mitabla; da el número de registros en la tabla