
class OOP():
	def __init__(self,lst):
		self.lst=list(filter(self.isEven,lst))
	def isEven(self,number):
		return number%2==0
	def give(self):
		return self.lst


app=OOP([1,2,3,4,5,6,7,8,9])
print(app.give())
