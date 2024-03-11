from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = b'abcdefghijklmnopqrstuvwxyzabcdef'
cipher = AES.new(key, AES.MODE_ECB)
#iv = cipher.IV
iv = get_random_bytes(16)
plaintext = b'AES top AES top '

#print("IV: ", iv)

ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

#new_plaintext = cipher.decrypt(ciphertext)
#print(new_plaintext)