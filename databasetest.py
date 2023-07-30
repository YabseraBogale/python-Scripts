import sqlite3

con=sqlite3.connect('Account.db')

con.execute(
"""
    create table if not exists  Account(
  	    website varchar(30) not null,
	    username varchar(20) not null,
  	    password varchar(30) not null,
  	    email varchar(30) not null
    );
"""

)
con.commit()