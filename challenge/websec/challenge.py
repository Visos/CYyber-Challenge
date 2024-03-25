from os import environ
from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
s = requests.Session()


url = 'http://web-14.challs.olicyber.it/'
text = s.get(url=url)
html_doc = text.text
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.find('b'))






























'''
INTRO 11
url2 = 'http://web-11.challs.olicyber.it/flag_piece'
login = 'login'
payload = {"username": "admin", "password": "admin"}
x = s.post(url=url+login, json= payload)
csrf = x.json()['csrf']
print(csrf)

for i in range (0,4):
    cookie = {'csrf': csrf , 'index' : i}
    x = s.get(url=url2, params=cookie)
    print(x.text)
    flag = flag +  x.json()['flag_piece']
    csrf =x.json()['csrf']

print(flag)

INTRO 13
url = 'http://web-13.challs.olicyber.it/'

text = s.get(url=url)
html_doc = text.text


soup = BeautifulSoup(html_doc, 'html.parser')
bro = soup.find_all('span')
for i in range (0, len(bro)):
    print(bro[i].contents[0], end = '')
'''