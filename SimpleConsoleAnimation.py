
import os
import time
msg="starting console"

for i in msg:
	mssg=msg.replace(i,i.upper())
	print(mssg)
	time.sleep(1)
	os.system("clear")
	
