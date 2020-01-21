# Problem: Implement Insertion Sort

def insertionSort(array):
	
   n = len(array)
	for i in range(1, n):
		
		idx = i
		while idx > 0 and array[idx] < array[idx-1]:
			swap(array, idx , idx-1)
			idx -= 1
		
	return array
			
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]
