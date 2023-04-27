from flask import Flask,request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app=Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

@app.route("/")
@limiter.limit("1/second") # maximum of 10 requests per minute
def index():
  return "Rate"


@app.route("/slow")
@limiter.limit("2 per day")
def slow():
    api_Info={
        "First Name":"Yabsera",
        "Last Name": "Bogale"

    }
    return api_Info




if __name__=="__main__":
    app.run(debug=True)