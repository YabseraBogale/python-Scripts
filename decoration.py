def testingdeco():
	return 1+1
	
@testingdeco
def test():
	return 1+1
	
print(test(5))
