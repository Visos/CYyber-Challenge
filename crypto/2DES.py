from Crypto.Cipher import DES

key1 = b'che bell'
key2 = b'a chiave'
plaintext = b'2DES meh'

cipher1 = DES.new(key1, DES.MODE_ECB)
half_ciphertext = cipher1.encrypt(plaintext)
print(half_ciphertext)

cipher2 = DES.new(key2, DES.MODE_ECB)
ciphertext = cipher2.encrypt(half_ciphertext)
print(ciphertext)

half_plaintext = cipher2.decrypt(ciphertext)
print(half_plaintext)

plaintext = cipher1.decrypt(half_plaintext)
print(plaintext)