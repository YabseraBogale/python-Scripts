"""

methods ==> camelCase
variables ==> small letters
author: Yabsera Bogale
Date:  01 April 2023

"""

import sqlite3


class Employees():

    self.pointer=sqlite3.connect('HumanMangaemntDatabase.db')
    self.obj=pointer.cursor()
    
    def makeTableEmployee():

        try:
            
            self.obj.execute(
                """
                    create table Employee(
                        emp_id int not null primary key,
                        first_name char(20) not null,
                        last_name char(20) not null,
                        salary int not null,
                        age int not null,
                        job_exper int not null
                    );
                """
            )
            self.pointer.commit()
            return "Successfully Made Employee Table"

        except sqlite3.Error as e:

            return e
    
    def laidOffEmployeeTable():
        
        try:
            self.obj.execute(
                """
                    create table laidOffEmployeeTable(
                        emp_id int not null,
                        first_name char(20) not null,
                        last_name char(20) not null,
                        salary float not null,
                        age int not null,
                        job_exper_at_Company int not null,
                        foreign key (emp_id) references Employee(emp_id)
                    )
                """
            )
            self.pointer.commit()
            return "Successfully Made Laid Off Employees Table"

        except sqlite3.Error as e:

            return e
    
    def laidOffEmployeeDataInseration(self,emp_id):
        try:
            self.data="select * from Employee where (empid=?);"
            self.obj.execute(self.data,(self.emp_id,))
            self.empolyeedata=self.obj.fetchall()
            return "Not FINISHED YET"
        except sqlite3.Error as e:

            return e
            

    def takeEmployessInfo():

        self.employee_Id=int(input("Enter Employee ID: "))
        self.first_name=input("Enter First Name: ")
        self.last_name=input("Enter Last Name: ")
        self.age=int(input("Enter Age: "))
        self.job_exp=int(input("Enter Job Experices: "))
        self.salary=float(input("Enter Salary: "))

        return (self.employee_Id,self.first_name,self.last_name,self.age,self.job_exp,self.salary)
    def sellAllEmployeeInformation():
        self.data="select * from Employee"
        self.obj.execute(data)
        self.value=self.obj.fetchall()
        for i in self.value:
            print(i)
    def setNewEmployessValues():

        try:

            self.values=self.takeEmployessInfo()
            self.insertion="insert into Employee(emp_id,first_name,last_name,age,job_exper,salary) values(?,?,?,?,?,?);"
            self.obj.execute(self.insertion,self.values)
            self.pointer.commit()
            return "Successfully Add into Table"

        except sqlite3.Error as e:
            return e
    


