from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

secret_string = b"super_secre"
key = b'abcdefghijklmnopqrstuvwxyzabcdef'

cipher = AES.new(key, AES.MODE_ECB)

#chosen plaintext scenario, ECB oracle
def oracle(plaintext):
	message_to_cipher = pad(plaintext + secret_string, 16)
	#print("DA DENTRO L'ORACOLO: messaggio da cifrare: ", message_to_cipher)
	#print(message_to_cipher)
	ciphertext = ""
	try:
		ciphertext = cipher.encrypt(message_to_cipher)
	except:
		print("Error")

	return ciphertext