from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'abcdefghijklmnop'
iv = b'prstuvwxyzabcdef' 

cipher = AES.new(key, AES.MODE_CBC, iv)
chipertext_secret = cipher.encrypt(pad(b"Bello", 16))
token = iv + chipertext_secret

def oracle(token):
    print("Il segreto può essere rivelato solo se il tuo nome passato inizia con C")
    u_iv = token[:16]
    token_name = token[16:]
    cipher = AES.new(key, AES.MODE_CBC, u_iv)
    decrypted = cipher.decrypt(token_name)
    decrypted_and_unpadded = unpad(decrypted, 16)
    print(decrypted_and_unpadded)
    if decrypted_and_unpadded.decode()[0] == 'C':
        return "Secret!"
    else:
        return "EH, VOLEVI!"