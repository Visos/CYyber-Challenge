from base64 import b64decode
import math

def xor(n1, n2):
    return bytes([x^y for x,y in zip(n1,n2)])
"""
z = 1976543456789

b = b'23456789876543'
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


"""
ESERCIZIO 4
m1 = "158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf" 
m2 = "73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2"

n1 = bytes.fromhex(m1)
n2 = bytes.fromhex(m2)

out = xor(n1,n2)
print(out)

"""
def xor_encryption(text, key):
    # Initialize an empty string for encrypted text
    encrypted_text = ""
    
    # Iterate over each character in the text
    for i in range(len(text)):
        encrypted_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    
    # Return the encrypted text
    return encrypted_text

# The plaintext that we want to encrypt
plain_text = bytearray.fromhex("104e137f425954137f74107f525511457f5468134d7f146c4c").decode()
# The secret key used for encryption
key = "20"

# Encrypt the plain_text using the key
encrypted_text = xor_encryption(plain_text, key)
# Print the encrypted text
print(f'Encrypted Text: {encrypted_text}')



ciphertext = "104e137f425954137f74107f525511457f5468134d7f146c4c"
chex = bytes.fromhex(ciphertext)
print(chex)

bytesdecode = bytearray.fromhex(ciphertext).decode()
print(bytesdecode)


l = '20'

bytekey = bytes.fromhex(l.encode().hex())*20
print(bytekey)

plain = xor(bytekey,chex)
print(plain)




ord('a')
chr(ord('a') + 3)   ##switcho il char

##print(encryptDecrypt(bytesdecode))

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
    
