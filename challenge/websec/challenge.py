from os import environ
from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
s = requests.Session()


url = 'http://web-16.challs.olicyber.it/'
text = s.get(url=url)
html_doc = text.text
soup = BeautifulSoup(html_doc, 'html.parser')

boiadio = ''

##trova tutte le NUOVE pagine linkate e le aggiunge a temp
def getpage(soup):
    all_page = soup.findAll('a')
    for i in range(0, len(all_page)):
        if all_page[i]['href'] not in pagelist:
            pagelist.append(all_page[i]['href'])

def checkh1(temp, url):
    for i in range(0, len(temp)):
        text = s.get(url=url+temp[i]).text
        soup = BeautifulSoup(text,'html.parser')
        allh1 = soup.find_all('h1')
        for j in range(0, len(allh1)):
            if 'flag' in allh1[j].contents:
                return allh1[j].contents
            
def find_flag(pagelist, i):
    if i< len(pagelist) and pagelist[i] not in read:
        read.append(pagelist[i])
        text = s.get(url=url+pagelist[i]).text
        soup = BeautifulSoup(text,'html.parser')
        allh1 = soup.find_all('h1')
        print(allh1[0].contents)
        if 'flag' in allh1[0].contents[0]:
            print(pagelist[i])
            return allh1[0].contents[0]
        getpage(soup)
    find_flag(pagelist, i+1)
    return 0


pagelist = []## lista di tutte le pagine 
temp = [] ## lista delle pagine aggiute e da visitare
read = []   ##pagine gia visitate
getpage(soup)         ##trova tutte le nuove pagine linkate e le aggiunge a temp

flag = find_flag(pagelist, 0)
print(flag)






























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