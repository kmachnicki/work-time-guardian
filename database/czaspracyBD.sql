CREATE TABLE Employee (Employee_ID  SERIAL NOT NULL, Tag_ID varchar(30) NOT NULL, First_Name varchar(30) NOT NULL, Last_Name varchar(50) NOT NULL, Email varchar(255) NOT NULL, Password varchar(50) NOT NULL, PRIMARY KEY (Employee_ID));
CREATE TABLE Passage (Passage_ID  SERIAL NOT NULL, EmployeeEmployee_ID int4 NOT NULL, timestamp timestamp NOT NULL, PRIMARY KEY (Passage_ID));
ALTER TABLE Passage ADD CONSTRAINT FKPassage686791 FOREIGN KEY (EmployeeEmployee_ID) REFERENCES Employee (Employee_ID);
