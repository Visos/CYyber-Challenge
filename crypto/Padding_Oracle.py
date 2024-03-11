from Secret_Padding_Oracle import chipertext_secret, oracle, iv
from paddingoracle import BadPaddingException, PaddingOracle

def is_padding_ok(msg):
	l = oracle(msg)
	print(l)
	return not b"Error" in l

class PadBuster(PaddingOracle):
	def __init__(self, **kwargs):
		super(PadBuster, self).__init__(**kwargs)

	def oracle(self, data, **kwargs):
		if is_padding_ok(data):
			return

		raise BadPaddingException

padbuster = PadBuster(max_retries=40)
solution = padbuster.decrypt(chipertext_secret, block_size=16, iv=iv)
print(solution.decode())