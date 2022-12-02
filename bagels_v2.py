import random

def main():
	number=random.randint(100,999)
	In_String_number=str(number)
	life=10
	Exit="E"
	while life>0 and Exit=="E":
		Guess_from_player=input("> ")
		if Guess_from_player=="e":
			Exit="e"
		else:
			if Guess_from_player==In_String_number:
				life+=1
				number=random.randint(100,999)
				In_String_number=str(number)
				Guess_from_player=input("> ")
			elif len(Guess_from_player)!=3:
				print("Enter The Right Digit")
			elif Guess_from_player.find(Guess_from_player[0]) == In_String_number.find(Guess_from_player[0]):
				print(">Fermi")
			elif Guess_from_player.find(Guess_from_player[1]) == In_String_number.find(Guess_from_player[1]):
				print(">Fermi")
			elif Guess_from_player.find(Guess_from_player[2]) == In_String_number.find(Guess_from_player[2]):
				print(">Fermi")
			elif Guess_from_player.find(Guess_from_player[0]) != In_String_number.find(Guess_from_player[0]) and In_String_number.find(Guess_from_player[0])!=-1:
				print(">Pico")
			elif Guess_from_player.find(Guess_from_player[1]) != In_String_number.find(Guess_from_player[1]) and In_String_number.find(Guess_from_player[1])!=-1:
				print(">Pico")
			elif Guess_from_player.find(Guess_from_player[2]) != In_String_number.find(Guess_from_player[2]) and In_String_number.find(Guess_from_player[2])!=-1:
				print(">Pico")
			else:
				print(">Bagels")
			life-=1
	print("Exiting")
if __name__=='__main__':
	print("Enter 3 Digit Number to Guess The number ")
	print("To Exit Enter \"e\"")
	main()
