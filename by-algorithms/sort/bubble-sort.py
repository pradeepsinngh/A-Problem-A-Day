

def bubbleSort(array):	
	n = len(array)
	swap = False
	while not swap:
		swap = True
		for j in range(n-1):
			if array[j] > array[j+1]:
				large = array[j]
				array[j] = array[j+1]
				array[j+1] = large
				swap = False
	return array
	
		
