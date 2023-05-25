--insert into ----------userInformation(first_Name,last_Name,Gender,Date_of_birth,email,jobExp,location,pd,education,id_passport,telephone)
--VALUES
--('yab','bog','Male',1997-02- 27,'yabserbgl@gmail.com',1,'Addiss Abebe','hash','./c/etudent/','./c/etudent/','0920205264');

create table userInformation(
	id int AUTOINCREMENT PRIMARY KEY,
	first_Name varchar(30) not null,
	last_Name varchar(30) not null,
	Gender varchar(10) not null,
	Date_of_birth datetime not null,
	email text not null,
	pd password not null, -- pd is for password
	id_passport text not null,
	telephone text not null

);