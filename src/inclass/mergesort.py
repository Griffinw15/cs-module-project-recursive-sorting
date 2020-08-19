# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    num_elements = len(arrA) + len(arrB)
    merged_arr = [0] * num_elements # allocating all the needed memory up-front

    # Your code here
    a = 0
    b = 0

    # for i in range(len(merged_arr)):
    #     if arrA[a] < arrB[b]:
    #         merged_arr[i] = arrA[a]
    #         a += 1
    #     elif arrA[a] >= arrB[b]:
    #         merged_arr[i] = arrB[b]
    #         b += 1

    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1

    # at this point, we've merged in all of the elements from 
    # one of the arrays, but not the other 
    
    # check both arrays to see if the pointer is still in range 
    # of its array 
    if a < len(arrA):
        # arrA still has leftover elements 
        # push them all to the merged array 
        merged_arr.extend(arrA[a:])

    if b < len(arrB):
        merged_arr.extend(arrB[b:])

    return merged_arr

# arrA = [3, 6, 8, 12, 15]
# arrB = [1, 4, 5, 9, 11]
# print(merge(arrA, arrB))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case: stop splitting the arrays in half when the arrays 
    # reach a length of 1 
    if len(arr) > 1:
    # otherwise, keep splitting them in half 
        left = merge_sort(arr[0 : len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2 : ])

        arr = merge(left, right)

    return arr

arr = [45, 12, 89, 14, 67, 45, 23, 90, 11]
print(merge_sort(arr))