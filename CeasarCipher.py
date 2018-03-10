'''Final Plan to add More Security by adding number encrpytion and '''
'''maybe security features like inverted alphabet order  '''

class CeasarCipher:

	''' CeasarCipher worked by shifting alphabets by some offset'''
	def __init__(self,enc_key):
		self.enc_key = enc_key
		self.enc_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2)

	def __crypt(self,msg,mode):
		if self.enc_key > 15:
			self.enc_key = self.enc_key % 15
		msg = msg.upper()
		enc_msg = []
		for char in msg:
			try:
				i = self.enc_list.index(char) # this will return ValueError if char is not in self.enc_list
				if mode == 'encrypt':
					enc_msg.append(self.enc_list[i + self.enc_key])
				elif mode == 'decrypt':
					enc_msg.append(self.enc_list[i - self.enc_key])
			except ValueError:
				enc_msg.append(char)
		return ''.join(map(str,enc_msg))

	
	def encrypt(self,msg):
		return self.__crypt(msg,'encrypt')

	def decrypt(self,msg):
		return self.__crypt(msg,'decrypt')

def ui_wrapper():
	while True:
		print('Welcome to ceasar cipher type key \n')
		while True:
			try:
				key = int(input('\t'))
				enc_model = CeasarCipher(key)
			except ValueError:
				print('\nEnter Valid Key in numbers')
				break
			while True:
				print('''
1. encryption
2. decryption
3. quit
				''')
				while True:
					try:
						inp = int(input('\n'))
						break
					except ValueError:
						print('Enter Valid option')
				if inp == 1:
					print('type in the string you want to encrpyt\n')
					enc_str = input('\t')
					print('Encrypted String : %s'%enc_model.encrypt(enc_str))
				if inp == 2:
					print('\ntype in the string you want to decrpyt\n')
					enc_str = input('\t')
					print('Decrypted String : %s'%enc_model.decrypt(enc_str))
				if inp == 3:
					exit()


if __name__ == '__main__':
	ui_wrapper()