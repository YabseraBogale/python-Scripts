from flask import Flask,request
app=Flask(__name__)




@app.route('/login',methods=['POST','GET'])
def login():
	if request.method=='POST':
		user_name=request.form['name']
		user_password=request.form['password']
		whattype=type(user_name)
		return f"User Name: {whattype}     Paasword: {user_password}"
	else:
		return "ok"
if __name__=='__main__':
	app.run(debug=True)
