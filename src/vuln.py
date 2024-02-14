from flask import Flask, request
from requests import get

app = Flask("MyApp")

@app.route("/")
def index():
    if request.args.get('name'):
        return "Hello " + request.args.get('name')
    return "Hello all..."

@app.route("/req")
def myrequests():
    url = request.args.get('url')
    res = get(url)
    return "<pre>" + res.text + "</pre>"


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
