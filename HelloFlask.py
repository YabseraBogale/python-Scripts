from flask import Flask

"""
	Instalizing Flask App
"""
app=Flask(__name__)

@app.route('/')
def index():
	
	return '<h1>Hello Flask %s</h1>' 
	
"""
Running Flask server

"""
if __name__=='__main__':
	app.run(debug=True)
