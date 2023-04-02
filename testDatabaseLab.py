import sqlite3

pointer=sqlite3.connect('testdb.db')
obj=pointer.cursor()

def makeTableEmployee():

    try:
            
        obj.execute(
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
        pointer.commit()
        return "Successfully Made Employee Table"
    except sqlite3.Error as e:
        return e

def laidOffEmployeeTable():
        
    try:
        obj.execute(
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
        pointer.commit()
        return "Successfully Made Laid Off Employees Table"

    except sqlite3.Error as e:
        return e

def takeEmployessInfo():
    employee_Id=int(input("Enter Employee ID: "))
    first_name=input("Enter First Name: ")
    last_name=input("Enter Last Name: ")
    age=int(input("Enter Age: "))
    job_exp=int(input("Enter Job Experices: "))
    salary=float(input("Enter Salary: "))
    return (employee_Id,first_name,last_name,age,job_exp,salary)

def sellAllEmployeeInformation():
    data="select * from Employee;"
    obj.execute(data)
    result=obj.fetchall()
    lst=[]
    for i in result:
        lst.append(i)
    return lst

def setNewEmployessValues():
    try:
        values=takeEmployessInfo()
        insertion="insert into Employee(emp_id,first_name,last_name,age,job_exper,salary) values(?,?,?,?,?,?);"
        obj.execute(insertion,values)
        pointer.commit()
        return "Successfully Add into Table"
    except sqlite3.Error as e:
        return e

def testingTupleDatabaseResult(databasetuple):
    lst=databasetuple
    for i in lst:
        for j in i:
            print("Data:",j,"\nData type:",type(j),"\n")
    return "Finshed"

#taking info for database and storing it => setNewEmployessValues()
data=sellAllEmployeeInformation()
#printing the data and database => print("Data in databse",data[0])
#seeing the data type => print("Data Type",type(data[0]))
# seeing the database internals => print(testingTupleDatabaseResult(data))
print(testingTupleDatabaseResult(data))