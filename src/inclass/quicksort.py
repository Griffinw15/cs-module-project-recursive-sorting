#the partition function handles the work of 
# selecting a pivot element and partitioning 
# the data in the array around that pivot 
# returns the left partition, the pivot, and the right partition
def partition(arr):
    # pick the first element as the pivot element 
    pivot = arr[0]
    left = []
    right = []

    # iterate through the rest of the array, putting each 
    # element in the appropriate bucket 
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    #returns wrapped in tuple
    return left, pivot, right

    ##alternate partition syntax
    #for num in arr:
    #    if num < pivot:
    #        left.append(num)
    #    if num > pivot:
    #        right.append(num)

def quicksort(arr):
    # base case 
    # if the length of the array is less than or equal to 1 
    if len(arr) <= 1:
        return arr
    # how do we get closer to our base case? 
    left, pivot, right = partition(arr)
    return quicksort(left) + [pivot] + quicksort(right)

arr = [13, 27, 5, 18, 3, 19, 22, 16]
arr = quicksort(arr)
print(arr)