
def Prime_factor(number):
	x = number
	if number == 1 or number ==0:
		return 'What are you giving'
	l = [] # List to contain Prime Factors
	while number % 2 == 0:
		l.append(2)
		number /= 2
	i = 3
	while i <= x:
		while number % i == 0:
			#print(i)
			l.append(i)
			number /= i
		i += 2
	if len(l) == 0:
		print('It is a prime number itself')
		return number
	return l 
'''Wrapper'''
def main():
	for i in range(100):
		print(Prime_factor(i))
main()
