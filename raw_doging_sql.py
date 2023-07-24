import sqlite3

connect=sqlite3.connect('database.db')


pointer=connect.cursor()


pointer.execute(
    """
        create table if not exists user_name(
            id int not null primary key,
            male varchar(20) not null,
            male_number int not null,
            female varchar(20) not null,
            female_number int not null
        );


    """
)

connect.commit()