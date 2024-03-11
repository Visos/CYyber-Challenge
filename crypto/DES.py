#install pycryptodome for Crypto -> https://pycryptodome.readthedocs.io/en/latest/src/installation.html

from Crypto.Cipher import DES

key = b'--key--I'
cipher = DES.new(key, DES.MODE_ECB)
plaintext = b'DES top '

ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

new_plaintext = cipher.decrypt(ciphertext)
print(new_plaintext)
