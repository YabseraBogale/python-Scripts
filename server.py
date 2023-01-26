from datetime import datetime
from flask import Flask
from flask import render_template
from requests import get
import json

app=Flask(__name__)

@app.route("/")
def CatsCollection():
	url="https://catfact.ninja/fact"
	fact=get(url).json()
	return render_template("CatsCollection.html",Fact=fact['fact'])

@app.route("/Cats")
def Cats():
	
	return render_template("Cats.html")


	
	
@app.route('/test')
def testing():
	url="https://catfact.ninja/fact"
	fact=get(url).json()
	return fact["fact"]
	



if __name__=="__main__":
	app.run(debug=True)
