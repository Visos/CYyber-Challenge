from Crypto.Cipher import DES

'''
key = b'\x01\x01\x01\x01\x01\x01\x01\x01'
cipher = DES.new(key, DES.MODE_ECB)
plaintext = b'DES top DES top '

ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

new_plaintext = cipher.encrypt(ciphertext)
print(new_plaintext)
'''


key1 = b'\x01\x1F\x01\x1F\x01\x0E\x01\x0E'
key2 = b'\x1F\x01\x1F\x01\x0E\x01\x0E\x01'

cipher1 = DES.new(key1, DES.MODE_ECB)
plaintext = b'DES top DES top '
ciphertext = cipher1.encrypt(plaintext)
print(ciphertext)

cipher2 = DES.new(key2, DES.MODE_ECB)
new_plaintext = cipher2.encrypt(ciphertext)
print(new_plaintext)


