import threading
import time
def test():
	ok=input("Enter")
	return ok
def Count(number):
	while number>0:
		number-=1
test1=threading.Thread(target=test)
test2=threading.Thread(target=Count,args=[10])
test1.start(timeout=3)
