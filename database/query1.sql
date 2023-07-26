CREATE DATABASE Library
USE Library

CREATE TABLE Autor (
	id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
	apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE,
    PRIMARY KEY (id)
);

CREATE TABLE Libro (
	id INT NOT NULL AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    fecha_publicacion DATE,
    autor_id int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (autor_id) REFERENCES Autor(id)
);
