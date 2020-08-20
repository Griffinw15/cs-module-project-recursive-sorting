# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start <= end:
        return -1
    
    else:
        mid = (start + end) // 2
    
        if target == arr[mid]:
            return mid

        elif target < arr[mid]:
            return binary_search(arr, target, start, mid - 1)
            #end = mid - 1

        elif target > arr[mid]:
            return binary_search(arr, target, mid + 1, end)
            #start = mid + 1


#def binary_search_recursive(arr, target, low, high):
#
#    middle = (low+high)/2
#
#    if len(arr) == 0:
#        return -1 # array empty
#
#    elif low > high:
#        return -1 # not found
#
#    elif arr[middle] == target:
#        return middle
#
#    else:
#        if target < arr[middle]:
#            high = middle-1 # eliminate RHS
#            
#        else:      
#            low = middle+1 # eliminate LHS
#        return binary_search_recursive(arr, target, low, high)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

