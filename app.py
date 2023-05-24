from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)


@app.route('/')
def home():

    return render_template("home.html")


@app.route('/signup',methods=['POST','GET'])
def signup():
    return render_template("regsister.html")

@app.route('/service')
def service():
    return render_template("service.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")






if __name__=="__main__":
    app.run(debug=True)
