'''Final Plan to add More Security by adding number encrpytion and '''
'''maybe security features like inverted alphabet order  '''

class CeasarCipher:

	''' CeasarCipher worked by shifting alphabets by some offset'''
	def __init__(self,enc_key):
		self.enc_key = enc_key
		self.enc_list = list('abcdefghijklmnopqrstuvwxyz' * 2)

	
	def encrypt(self,msg):
		if self.enc_key > 15:
			self.enc_key = self.enc_key % 15
		msg = msg.lower()
		enc_msg = []
		for char in msg:
			try:
				i = self.enc_list.index(char) # this will return ValueError if char is not in self.enc_list
				enc_msg.append(self.enc_list[i + self.enc_key])
			except ValueError:
				enc_msg.append(char)
		return ''.join(map(str,enc_msg))

	def decrypt(self,msg):
		if self.enc_key > 15:
			self.enc_key = self.enc_key % 15
		msg = msg.lower()
		enc_msg = []
		for char in msg:
			try:
				i = self.enc_list.index(char)
				enc_msg.append(self.enc_list[i - self.enc_key])
			except ValueError: # when char is not alphabet
				enc_msg.append(char)
		return ''.join(map(str,enc_msg))


if __name__ == '__main__':
	enc = CeasarCipher(4)
	enc_str = enc.encrypt('myName is anonymouse 007')
	print('Encrypter string : %s'%enc_str)
	print('Decrypted string : %s'%enc.decrypt(enc_str))


