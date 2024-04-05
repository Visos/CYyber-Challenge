import math

def xgcd(a,b):
    r0, r1 = a, b
    s0, s1, t0, t1 = 1, 0, 0, 1
    while r1 != 0:
        r0, r1 = divmod(r1,r0)     
        a, b = b, r
        s0, s1 = s1, s0 - q *s1
        t0, s1 = t1, t0 - q *t1
        q, r = divmod(a,b)
        if r ==0 : break
    return b ,s0, t0


##print (xgcd(a,b))


#pow(2,19, 31)       # con il terzo termine si indica il modulo
#pow( 2, -1 , 7)     # -1 indica trova l'inverso

a =196
b = 175

div = math.gcd(a, b)

a = a // div
b = b//div
print(a)
x = pow (a, -1 , b)
print(x)
    
    
(80,77)    #dividiamo per il massimo comune divisore
            #invertimao i risultati
math.gcd()  # per vedere se sono coprimi
'''divido per il gcd
trovo l'inverso
   '''    
