from Secret_Byteflipping import token, oracle

iv = token[:16]  ##stringa di cripting
ciphered_name = token[16:]

print(iv)
print(iv.hex())
iv_bit_list = list("".join([bin(int(c, 16))[2:].zfill(4) for c in iv.hex()]))
print(iv_bit_list)
iv_bit_list[7] = '1'
print(iv_bit_list)
iv = [int("".join(iv_bit_list[i:i+4]),base=2) for i in range(0, len(iv_bit_list), 4)]
iv = "".join([hex(c)[2:] for c in iv])
print(iv)
iv = bytes.fromhex(iv)
print(iv)
secret = oracle(iv+ciphered_name)
print(secret)