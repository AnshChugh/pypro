'''
Insertion Sort arranges given array in ascending order using insertion sort algorithm
	Puesocode:
		insertion-sort A:
		for i <- 1 to length(A)
			j <- i
			while j > 0 and A[j-1] > A[j]:
				swap A[j] and A[j-1]
				j <- j-1

'''
def insertion_sort(arr):
	for i in range(len(arr)):
		j = i
		while j > 0 and arr[j-1] > arr[j]:
			arr[j],arr[j-1] = arr[j-1],arr[j]
			j -= 1
	return arr

def test():
	from random import randint
	arr = []
	for i in range(30):
		arr.append(randint(0,100))
	print(arr)
	arr_asc = insertion_sort(arr)
	print(arr_asc)

if __name__ == '__main__':
	test()