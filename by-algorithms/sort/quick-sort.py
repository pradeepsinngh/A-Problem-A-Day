# Implement Quick Sort

def quickSort(array):
    # Write your code here.
	
	startIdx = 0
	endIdx = len(array) -1
	quickSortHelper(startIdx, endIdx, array)
	return array

def quickSortHelper(start, end, array):
	if start >= end:
		return
	
	pivot = start
	left = start + 1
	right = end
	
	while left <= right:
		if array[left] > array[pivot] and array[right] < array[pivot]:
			swap(left, right, array)
		elif array[left] <= array[pivot]:
			left += 1
		elif array[right] >= array[pivot]:
			right -= 1
			
	swap(right, pivot, array)
	leftSubarraySmaller = (right - 1 - start) < (end - right + 1)
	
	if leftSubarraySmaller:
		quickSortHelper(start, right -1, array)
		quickSortHelper(right+1, end, array)
	else:
		quickSortHelper(right+1, end, array)
		quickSortHelper(start, right -1, array)
		
	
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
