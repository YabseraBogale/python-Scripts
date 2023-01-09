import streamlit as st
from streamlit_option_menu import option_menu

select=option_menu(
	menu_title=None,
	options=["Home","Contact","Gallery","Sales"],
	orientation="horizontal",
	styles={
  
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link-selected": {"background-color": "green"},
    },
	)
	
	
if select=="Home":
	st.write("Welcome")
if select=="Contact":
	st.write("Contact info")
if select=="Gallery":
	st.write("Image Gallery")
if select=="Sales":
	st.write("Sales")
