from flask import render_template



def home_page():
	
	return render_template("home.html")
	
def movies_page():
	
	return render_template("Movie.html")
