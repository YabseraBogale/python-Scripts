import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def Collatzsequence(number):
	lst=[]
	if number==1:
		lst.append(number)
		return lst
	while number!=1:
		if number%2==0:
			number=int(number/2)
			lst.append(number)
		else:
			number=int((3*number)+1)
			lst.append(number)

	return lst

st.title("COLLATZ SEQUENCE")




st.write("""
	The Collatz sequence, also called the 3n + 1
	problem, is the simplest impossible math
	problem. (But don’t worry, the program
	itself is easy enough for beginners.) From a
	starting number, n, follow three rules to get the next
	number in the sequence:
	"""
)
st.write("""
	\n\t1. If n is even, the next number n is n / 2.
	\n2. If n is odd, the next number n is n * 3 + 1.
	\n3. If n is 1, stop. Otherwise, repeat.
	\nIt is generally thought, but so far not mathematically proven, that
	every starting number eventually terminates at 1. More information
	about the Collatz sequence can be found at https://en.wikipedia.org/wiki/Collatz_conjecture.
	\n for example
""")

number=st.text_input(label="Enter Number",placeholder="12")
if number.isdecimal():
	num=number
	number=int(number)
	numberStr=str(Collatzsequence(number)).replace("[","").replace("]","")
	st.write(f"Collatz sequence of the number {num}:")
	st.write((f"\t{numberStr}"))
	number=np.array(Collatzsequence(number))
	st.write(f"Max number in The series is {number.max()} \n The distribution map of the sequnce is")
	fig, x = plt.subplots()
	x.hist(number,bins=10)
	st.pyplot(fig)

st.write("in conclusion")
