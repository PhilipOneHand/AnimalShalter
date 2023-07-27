CREATE DATABASE IF NOT EXISTS Animal_Shelter;
CREATE TABLE Cats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    breed VARCHAR(255),
    color VARCHAR(255),
    age INT,
    vaccinated ENUM('yes', 'no'),
    castrated ENUM('yes', 'no')
);
USE Animal_Shelter;
CREATE TABLE Dogs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    breed VARCHAR(255),
    color VARCHAR(255),
    age INT,
    vaccinated ENUM('yes', 'no'),
    castrated ENUM('yes', 'no')
);
INSERT INTO Dogs (breed, color, age, vaccinated, castrated)
VALUES ('Labrador Retriever', 'Golden', 3, 'yes', 'no');

INSERT INTO Cats (breed, color, age, vaccinated, castrated)
VALUES ('Siamese', 'White', 2, 'yes', 'no');
USE Animal_Shelter;
CREATE TABLE Other (
    id INT AUTO_INCREMENT PRIMARY KEY,
    animal VARCHAR(255),
    age INT,
    vaccinated ENUM('yes', 'no')
);
INSERT INTO Other (animal, age, vaccinated)
VALUES ('Bird', 1, 'no');