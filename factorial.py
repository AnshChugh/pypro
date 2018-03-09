'''This supports both negative and positive factorial'''

def factorial_recursion(number):
	if number == 1:
		return 1
	if number == -1:
		return -1
	if number > 1:
		return number * factorial_recursion(number - 1)
	if number < 1:
		return number * factorial_recursion(number + 1) 

print(factorial_recursion(4))

def factorial_loop(number):
	if number == 1:
		return 1
	if number == -1:
		return -1
	if number > 1:
		y = number 
		while y > 1:
			number = number * (y - 1)
			y -= 1
	if number < 1:
		y = number
		while y < -1:
			number = number * (y+1)
			y += 1
	return number

print(factorial_loop(6))
print(factorial_loop(-3))
