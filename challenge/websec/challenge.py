from os import environ
from flask import Flask, Response
import requests


app = Flask(__name__)



url = 'http://web-06.challs.olicyber.it/token'
url2 = 'http://web-06.challs.olicyber.it/flag'


s = requests.Session()

##a = {'Accept': 'application/xml'}
##password={'password': 'admin'}
s.get(url)

x = s.get(url=url2)
print(x)
print(x.content)



bro = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"
ris = bytes.fromhex(bro)
print(ris)

