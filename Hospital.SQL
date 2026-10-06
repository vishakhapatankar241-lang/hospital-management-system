create database hospitaldb;
use hospitaldb;
create table users(
id int primary key auto_increment,
username varchar(50),
passwod varchar(50),
role varchar(50));
create table patient(
patient_id int primary key auto_increment,
name varchar(50),
age int,
gender varchar(50),
disease varchar(150)
);
insert into users(username,passwod,role)
values("Admin","Admin123","Admin"),
("Doctor","Doctor123","Doctor"),
("Patient","Patient123","Patient"),
("Chemist","Chemist123","Chemist")
;
desc users;
desc patient;
show databases;
show tables;
select* from users;
select* from patient;



