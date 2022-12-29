import streamlit as st
from time import sleep
from random import randint
import numpy as np

def make():
	lst=[]
	i=0
	while i<20:
		j=0
		lst2=[]
		while j<20:
			lst2.append(randint(0,1))
			j+=1
		lst.append(lst2) 
		i+=1
	return np.array(lst)


st.write(make())
st.empty()
