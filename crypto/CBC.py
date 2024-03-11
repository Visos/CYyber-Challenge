from Crypto.Cipher import DES3, AES

key = b'abcdefghijklmnopqrstuvwx'
cipher = DES3.new(key, DES3.MODE_CBC)
plaintext = b'DES3 ok DES3 ok DES3 ok DES3 ok '
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

#cipher = DES3.new(key, DES3.MODE_CBC, cipher.iv)
#new_plaintext = cipher.decrypt(ciphertext)
#print(new_plaintext)

#print("IV: ", cipher.iv)

'''
key = b'abcdefghijklmnopqrstuvwxyzabcdef'
cipher = AES.new(key, AES.MODE_CBC)
plaintext = b'AES top AES top '
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

cipher = AES.new(key, AES.MODE_CBC, cipher.iv)
new_plaintext = cipher.decrypt(ciphertext)
print(new_plaintext)

print("IV: ", cipher.iv)
'''
#tipicamente, viene ritornato iv+ciphertext