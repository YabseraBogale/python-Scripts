import asyncio

async def test():
	name=input('Enter Name: ')
	return name
	
async def counting():
	task=asyncio.create_task(test())
	
	

asyncio.run(counting())
""""
Failed to for seting time out on input

"""
