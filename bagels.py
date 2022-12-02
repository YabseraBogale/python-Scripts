import random

def main():
	number=random.randint(100,999)
	In_String_number=str(number)
	life=10
	while life>0:
		Guess_from_player=input("Guess The Number: ")
		if Guess_from_player==In_String_number:
			life+=1
			number=random.randint(100,999)
			In_String_number=str(number)
			Guess_from_player=input("Guess The Number: ")
		for i in Guess_from_player:
			if Guess_from_player.find(i) == In_String_number.find(i):
				print("Fermi")
			elif Guess_from_player.find(i) != In_String_number.find(i) and In_String_number.find(i)!=-1:
				print("Pico")
			else:
				print("Bagels")
		life-=1
	print("You Loss")
if __name__=='__main__':
	print("Enter 3 Digit Number to Guess The number")
	main()
