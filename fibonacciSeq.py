''' Fibinocci Sequence is the third number is sum of last two numbers '''
''' like 1,1,2,3,5,8,... to the n'th digit '''

def FibnocciSeq(n_digit):
	if n_digit > 1000:
		return "Could You even see 1000 numbers Idiot"
	if n_digit == 0:
		return 0
	if n_digit == 1:
		return [1]
	if n_digit == 2:
		return [1,1]
	a = 1
	l = [1,1]
	b = 1
	for i in range(n_digit - 2):
		a, b = b , a + b 
		l.append(b)
	if n_digit == 0:
		return 0
	if n_digit == 1:
		return [1]
	if n_digit == 2:
		return [1,1]
	return l

'''Wrapper Function'''
def main():
	print("Fibinocci Sequence till the n'th digit\n")
	print('\n\n numbers=%s'%str(FibnocciSeq(1)))

if __name__ == '__main__':
	main()