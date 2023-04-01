import sqlite3

def MakeDatabase():
    pointer=sqlite3.connect('StudentDatabase.db')
    obj=pointer.cursor()
    return [pointer,obj]

def MakeTable(pointer,obj):
    obj.execute("""
                create table Grade(
                    student_Id int not null primary key,
                    first_name char(20) not null,
                    last_name char(20) not null,
                    student_Grade char(3) not null

                );
        """)
    pointer.commit()
    return "Successfully Made Table"

def StudentInfo():
    student_Id=int(input("Enter Student ID: "))
    first_name=input("Enter First Name: ")
    last_name=input("Enter Last Name: ")
    student_Grade=input("Enter Student Grade: ")
    lst=[student_Id,first_name,last_name,student_Grade]
    return lst

    
def InsertIntoTable(datalist,studentInfo):
    datalist[1].execute(f"""
                insert into Grade(student_Id,first_name,last_name,student_Grade)
                values
                ({studentInfo[0]},'{studentInfo[1]}','{studentInfo[2]}','{studentInfo[3]}');
        """
                )
    datalist[0].commit()
    return f"Successfully inserted {studentInfo[1]} {studentInfo[2]}"


def seeAllStudentInfo(datalist):
    datalist[1].execute("""
                select * from Grade;
        """)
    datalist[0].commit()

    result=datalist[1].fetchall();
    lst=[]
    for i in result:
        lst.append(i)
    return lst

    
# for this pc the database has been made for other pc use this => database=MakeDatabase()
# for this pc the table has been made for other pc use this => table=MakeTable(database[0],database[1])
# for this pc the table has been made for other pc use this => database=MakeDatabase()
# for this pc the table has been made for other pc use this => studentinfo=StudentInfo()
# for this pc the table has been made for other pc use this => insertion=InsertIntoTable(database,studentinfo)
# for this pc the table has been made for other pc use this => database=MakeDatabase()
# for this pc the table has been made for other pc use this => print(seeAllStudentInfo(database))
