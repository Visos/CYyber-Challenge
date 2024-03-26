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

# copia tutte le pagine nella lista delle pagine visitate
def getpage(all_page, temp):
    for i in range(0, len(all_page)):
        if all_page[i]['href'] not in pagelist:
            temp.append(all_page[i]['href'])

def checkpages(temp, url):
    for i in range(0, len(temp)):
        text = s.get(url=url+temp[i]).text
        soup = BeautifulSoup(text,'html.parser')
        allh1 = soup.find_all('h1')
        print('all h1 = ', allh1)
        for j in range(0, len(allh1)):
            if 'flag' in allh1[j].contents:
                return allh1[j].contents


pagelist = []## lista di tutte le pagine visitate
temp = [] ## lista delle pagine aggiute e da visitare
all_page = soup.findAll('a')
getpage(all_page, temp)         ##trova tutte le nuove pagine linkate e le aggiunge a temp
checkpages(temp, url)           ##chek degli h1 di temp

for i in range(0, len(temp)):
    text = s.get(url=url+temp[i]).text


    
pagelist = pagelist+ temp
































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