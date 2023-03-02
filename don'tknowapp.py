import streamlit as st
import streamlit_authenticator as stauth

with st.form("my_form"):
   st.write("Sign up form")
   firstName = st.text_input("First Name")
   middleName = st.text_input("Middle Name")
   lasttName = st.text_input("Last Name")
   email=st.text_input("Email")
   pd=st.text_input("password",type="password")
   re_pd=st.text_input("re enter password",type="password")
   
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if pd==re_pd:
       password=stauth.Hasher(pd).generate()
   else:
	   st.warning("Enter the same password")

   
