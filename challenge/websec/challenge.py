from os import environ
from flask import Flask, Response
import requests


app = Flask(__name__)



url = ' http://web-11.challs.olicyber.it/'
url2 = 'http://web-11.challs.olicyber.it/flag_piece'
flag = 'flag_piece/'
login = 'login'


s = requests.Session()
payload = {"username": "admin", "password": "admin"}

x = s.post(url=url+login, json= payload)
csrf = x.json()["csrf"]
print(x.cookies)


x = s.get(url=url2, params=csrf)
print(x.text)
#print(csrf1)
