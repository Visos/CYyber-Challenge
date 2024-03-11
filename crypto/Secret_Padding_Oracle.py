from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'abcdefghijklmnop'
iv = b'qrstuvwxyzabcdef' 

cipher = AES.new(key, AES.MODE_CBC, iv)
chipertext_secret = cipher.encrypt(pad(b"Secret!", 16))

def oracle(ciphertext):
    while True:
        try:
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = cipher.decrypt(ciphertext)
            decrypted_and_unpadded = unpad(decrypted, 16)
            return decrypted_and_unpadded #ci aspettiamo che il segreto non contenga "Error"
        except Exception as e:
            return b"Error"