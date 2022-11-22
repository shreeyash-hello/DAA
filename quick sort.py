import random

def quicksort(arr, start , stop):
    if(start < stop):
        pivotindex = partitionrand(arr,start, stop)
        quicksort(arr , start , pivotindex-1)
        quicksort(arr, pivotindex + 1, stop)

def partitionrand(arr , start, stop):
    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)

def partition(arr,start,stop):
    pivot = start
    i = start + 1 
    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)

if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    quicksort(array, 0, len(array) - 1)
    print(array)

    
    ##########################################################################
    
def partition(array, low, high):
	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1

def quick_sort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		quick_sort(array, low, pi - 1)
		quick_sort(array, pi + 1, high)
    
array = [10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)
print(f'Sorted array: {array}')
