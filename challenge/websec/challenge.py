from os import environ
from flask import Flask, Response
import requests


app = Flask(__name__)

"""
@app.route("/")
def index():
    return Response(environ["FLAG"], mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
"""

url = 'http://web-05.challs.olicyber.it/flag'

a = {'Accept': 'application/xml'}
password={'password': 'admin'}

x = requests.get(url=url, cookies=password)
print(x)
print(x.content)