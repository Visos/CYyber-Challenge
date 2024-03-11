from Crypto.Cipher import AES
from secret_ECB_Oracle import oracle

#Assume that the secret is long 16bytes

chosen_plaintext = b"aaaaaaaaaaaaaaa"
found_secret = ""

for byte_guess_position in range(15, 14, -1):
	#print("POS ", byte_guess_position)
	plaintext = chosen_plaintext[:(byte_guess_position)]
	print("Porzione considerata del plaintext: ", plaintext)
	ciphertext = oracle(plaintext)
	print("Chipertext obbiettivo: ", ciphertext[:15])
	for byte_guess in range(256):
		guess_plaintext = plaintext + found_secret.encode() + byte_guess.to_bytes(1, 'little')
		new_ciphertext = oracle(guess_plaintext)
		if(ciphertext[:15] == new_ciphertext[:15]):
			print("Trovato byte target: ", byte_guess.to_bytes(1, 'little').decode(), " da plaintext ", guess_plaintext.decode(), " che da ciphertext ", new_ciphertext[:15])
			found_secret = found_secret + byte_guess.to_bytes(1, 'little').decode()
			break

print(found_secret)