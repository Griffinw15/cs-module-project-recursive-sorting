# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    num_elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here
    a = 0
    b = 0

    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            #move index along if you took the value
            a += 1
        else:
            #opposite case
            merged_arr.append(arrB[b])
            b += 1

    if a < len(arrA):
        # arrA still has leftover elements 
        # push them all to the merged array 
        merged_arr.extend(arrA[a:])
​
    if b < len(arrB):
        merged_arr.extend(arrB[b:])

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    n = len(arr)

    if n >= 1:

        left = merge_sort(arr[:n // 2])
        right = merge_sort(arr[n // 2:])

        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here