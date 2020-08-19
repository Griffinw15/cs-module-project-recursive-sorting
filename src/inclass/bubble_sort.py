def bubble_sort(arr):
    # we know all the elements are in sorted order when we do a full
    # pass through the array and perform no swaps 
    swaps_occurred = True
    # iterating through the arr and looking at elements two at a time 
    # swapping them if they're out of order 
    while swaps_occurred:
        swaps_occurred = False
        # if we do this all the way through, all the elements will 
        # eventually end up in sorted order 
        for i in range(len(arr) - 1):
            # we need to swap if arr[i] > arr[i+1]
            if arr[i] > arr[i+1]:
                # swap them
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occurred = True
    
    return arr

arr = [5,1,7,6,2,1,0]
# print(bubble_sort(arr))

    # parallel to selection sort: builds up the sorted portion of the array 
    # starting by putting the largest element at the end of the array,
    # second-largest at the second-to-last spot, etc. 

    # the number of iterations through the array that we need to make is equal 
    # to the number of elements in the array - O(n^2)

def recursive_bubble_sort(arr, unsorted_length):
    # base case(s)
    # re-use the swaps_occurred boolean idea 
    # the boolean tells us when the "unsorted" portion of the list reaches 0 
    # if the length of the unsorted portion is 0 
    # how do we get closer to a base case? 
    # each pass shortens the unsorted portion by 1 
    # each pass does the exact same thing as what it in the iterative implementation 
    for i in range(unsorted_length - 1):
        # we need to swap if arr[i] > arr[i+1]
        if arr[i] > arr[i+1]:
            # swap them
            arr[i], arr[i+1] = arr[i+1], arr[i]

    if unsorted_length > 0:
        recursive_bubble_sort(arr, unsorted_length - 1)

# arr = [13, 15, 6, 18, 3, 27, 19, 22]
# arr = [5,1,7,6,2,1,0]
recursive_bubble_sort(arr, len(arr))
print(arr)