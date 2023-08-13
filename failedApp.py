
# Falied to make it desktop go for another method or use webview purely

from flask import Flask
import webview


app=Flask(__name__)


@app.route('/')
def index():
	return "Hello World"
	
def server_start():
	app.run()

if __name__=="__main__":
	webview.start(target=server_start)
