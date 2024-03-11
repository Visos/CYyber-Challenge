from Crypto.Cipher import AES
from Crypto.Util import strxor

iv = b'abcdefghijklmnop'
key = iv

cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = b'AESutopuAESutopuAESutopuAESutopu'
plaintext = cipher.decrypt(ciphertext)
print(plaintext)

iv = strxor.strxor(strxor.strxor(plaintext[:16], plaintext[16:]), ciphertext[:16])
print("IV: ", iv.decode())