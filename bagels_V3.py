import random

def main():
	number=random.randint(100,999)
	In_String_number=str(number)
	life=10
	Exit="E"
	while life>0 and Exit=="E":
		Guess_from_player=input("\t> ")
		if Guess_from_player=="e":
			Exit="e"
		elif Guess_from_player.isdecimal()==False:
			print("\tEnter 3 Digit number not character")
			main()
		else:
			if Guess_from_player==In_String_number:
				life+=1
				print("\tYou Won \n\tlife point",life)
				number=random.randint(100,999)
				In_String_number=str(number)
				Guess_from_player=input("\t> ")
			elif len(Guess_from_player)!=3:
				print("\tEnter The Right Digit")
			elif Guess_from_player.find(Guess_from_player[0]) == In_String_number.find(Guess_from_player[0]):
				print("\t> Fermi")
			elif Guess_from_player.find(Guess_from_player[1]) == In_String_number.find(Guess_from_player[1]):
				print("\t> Fermi")
			elif Guess_from_player.find(Guess_from_player[2]) == In_String_number.find(Guess_from_player[2]):
				print("\t> Fermi")
			elif Guess_from_player.find(Guess_from_player[0]) != In_String_number.find(Guess_from_player[0]) and In_String_number.find(Guess_from_player[0])!=-1:
				print("\t> Pico")
			elif Guess_from_player.find(Guess_from_player[1]) != In_String_number.find(Guess_from_player[1]) and In_String_number.find(Guess_from_player[1])!=-1:
				print("\t> Pico")
			elif Guess_from_player.find(Guess_from_player[2]) != In_String_number.find(Guess_from_player[2]) and In_String_number.find(Guess_from_player[2])!=-1:
				print("\t> Pico")
			else:
				print("\t> Bagels")
			life-=1
	print("Exiting")
if __name__=='__main__':
	print("\tEnter 3 Digit Number to Guess The number ")
	print("\tTo Exit Enter \"e\"")
	main()
