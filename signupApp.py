from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/login')
def Login():
	return render_template("logintest.html")
@app.route('/signup',methods=['POST','GET'])
def SignUp():
	if request.method=='POST':
		name=request.form['name']
		email=request.form['email']
		if request.form['password']==request.form['repassword']:
			password=request.form['password']
			if request.form.get('yes')=='on':
				return f"Welcome {name} "
			else:
				return "can't use with out terms of service"
		else:
			return render_template("SignupPage.html",pd="Password must Match")
	else:
		return "404"
		
	
if __name__=="__main__":
	app.run(debug=True)
