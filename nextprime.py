''' To find next prime '''
''' This only work after 11'''
from math import sqrt as sqrt
def next_prime(starting_point):
	x = starting_point
	while True:
		if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0 or  x == abs(sqrt(x)) ** 2:
			if x < 10:
				return starting_point
			x += 1
		else:
			break
	return x
''' Wrapper UI '''
def ui():
	print('I am lazy :-) do it yourself')
