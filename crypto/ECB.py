from Crypto.Cipher import DES3

key = b'abcdefghijklmnop'
cipher = DES3.new(key, DES3.MODE_ECB)
plaintext = b'DES3 ok DES3 ok '

ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

new_plaintext = cipher.decrypt(ciphertext)
print(new_plaintext)

