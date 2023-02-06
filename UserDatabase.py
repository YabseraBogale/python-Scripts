import sqlite3

class User_database():
	def __init__(self):
		self.db=sqlite3.connect('UserDatabase.db') 
		self.curr=db.cursor()
	def CheckUserInDatabase(self,user_name):
		self.curr.execute(f"Select UserName from UserTable Where UserName={user_name};")
		self.TrueUser=self.curr.fetchall()
		return len(self.TrueUser)
	def PassWordCheck(self,Password,user_name):
		if(CheckUserInDatabase(user_name)==1):
			self.curr.execute(f"Select UserPassWord from UserTable Where UserName={PassWord};")
			self.TruePassWord=self.curr.fetchall()
		
