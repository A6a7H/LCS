def partitionHoare(arr, low, high):
	i = low
	j = high
	mid_item = arr[low + (high - low)//2]
	while i <= j:
	    while arr[i] < mid_item: i += 1
	    while arr[j] > mid_item: j -= 1
	    if i < j:
	        arr[i], arr[j] = arr[j], arr[i]
	        i += 1
	        j -= 1
	    else:
	    	return j
	return j

def partitionLomuta(arr, low, high):
	i = low
	j = high
	mid = low + (high - low)//2
	mid_item = arr[mid]
	arr[mid], arr[high] = arr[high], arr[mid]
	store = low
	for i in range(low, high):
		if arr[i] < mid_item:
			arr[i], arr[store] = arr[store], arr[i]
			store += 1
	arr[high], arr[store] = arr[store], arr[high]
	return store

def kthstatistic(arr, low, high, k_order):
	while low != high:
		pivot = partitionHoare(arr, low, high)
		if k_order == pivot:
			return arr[pivot]
		if k_order < pivot: high = pivot
		else: low = pivot+1
	return arr[low]

# arr = [1, 2, 3, 3, 4, 0, 5, 6, 7, 8, 0, 10, 15]
arr = [1,2,3,4,5,6,7,8]
print(kthstatistic(arr, 0, len(arr)-1, 1))