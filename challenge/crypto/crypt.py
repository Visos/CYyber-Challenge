from base64 import b64decode
import math

z = 1976543456789

b = b'23456789876543'
"""
a = int.from_bytes(b, 'big')
y =  (z).to_bytes(n, 'big')
"""
"""
    ESERCIZIO 3
n = 664813035583918006462745898431981286737635929725
y =  (n).to_bytes(20, 'big')
s = 'ZmxhZ3t3NDF0XzF0c19hbGxfYjE='
print(b64decode(s))
print(y)
    
"""
def xor(n1, n2):
    return bytes([x^y for x,y in zip(n1,n2)])


"""
ESERCIZIO 4
m1 = "158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf" 
m2 = "73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2"

n1 = bytes.fromhex(m1)
n2 = bytes.fromhex(m2)

out = xor(n1,n2)
print(out)

"""

ciphertext = "104e137f425954137f74107f525511457f5468134d7f146c4c"
p1 = bytes.fromhex(ciphertext)
dictionary = {}

bytesdecode = bytearray.fromhex(ciphertext).decode()
print(bytesdecode)

key = 20
key1 = key.to_bytes(1,'big')
key1 = key1+key1+key1+key1+key1+key1+key1+key1+key1+key1+key1




'''for n in range (0,256):
    y =  (n).to_bytes(1, 'big')
    b = b''
    for i in range (0,12):
        b = b + y
        ##print(b)
    p2 = xor(p1,b)
    dictionary[n] = p2
    plaintext = p2.hex()
    print(plaintext)
'''
    
