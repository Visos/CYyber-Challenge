from Crypto.Cipher import DES

ciphertext = b'q\x9fo\xa2\x98h\x84H'
plaintext = b'2DES meh'

dictionary_keys = {}

print("First step")
for int1 in range(0, 256):
	byte1 = int1.to_bytes(1, 'big')
	for int2 in range(0, 256):
		byte2 = int2.to_bytes(1, 'big')
		for int3 in range(0, 256):
			byte3 = int3.to_bytes(1, 'big')
			for int4 in range(0, 256):
				byte4 = int4.to_bytes(1, 'big')
				for int5 in range(0, 256):
					byte5 = int5.to_bytes(1, 'big')
					for int6 in range(0, 256):
						byte6 = int6.to_bytes(1, 'big')
						for int7 in range(0, 256):
							byte7 = int7.to_bytes(1, 'big')
							for int8 in range(0, 256):
								byte8 = int8.to_bytes(1, 'big')
								key1 = byte1 + byte2 + byte3 + byte4 + byte5 + byte6 + byte7 + byte8

								cipher1 = DES.new(key1, DES.MODE_ECB)
								dictionary_keys[cipher1.encrypt(plaintext)] = key1

print("Secondo step")
for int1 in range(0, 256):
	byte1 = int1.to_bytes(1, 'big')
	for int2 in range(0, 256):
		byte2 = int2.to_bytes(1, 'big')
		for int3 in range(0, 256):
			byte3 = int3.to_bytes(1, 'big')
			for int4 in range(0, 256):
				byte4 = int4.to_bytes(1, 'big')
				for int5 in range(0, 256):
					byte5 = int5.to_bytes(1, 'big')
					for int6 in range(0, 256):
						byte6 = int6.to_bytes(1, 'big')
						for int7 in range(0, 256):
							byte7 = int7.to_bytes(1, 'big')
							for int8 in range(0, 256):
								byte8 = int8.to_bytes(1, 'big')
								key2 = byte1 + byte2 + byte3 + byte4 + byte5 + byte6 + byte7 + byte8

								cipher2 = DES.new(key2, DES.MODE_ECB)
								if cipher2.decrypt(ciphertext) in dictionary_keys.keys():
									print("Chiavi trovate:")
									print("k1: ", dictionary_keys[cipher2.decrypt(ciphertext)])
									print("k2: ", key2)
								else: 
									print("ERROR: chiavi")