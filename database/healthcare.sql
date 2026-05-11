CREATE DATABASE healthcare_db;
USE healthcare_db;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(100),
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(20)
);
CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    contact VARCHAR(20),
    address TEXT
);
CREATE TABLE appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    appointment_date DATE,
    doctor VARCHAR(100),
    status VARCHAR(50),
    FOREIGN KEY (patient_id) REFERENCES patients(id)
);
CREATE TABLE medical_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    diagnosis TEXT,
    treatment TEXT,
    record_date DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(id)
);
CREATE TABLE staff (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(100),
    position VARCHAR(100),
    contact VARCHAR(20),
    email VARCHAR(100)
);