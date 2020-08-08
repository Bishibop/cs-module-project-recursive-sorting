# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    i = 0
    j = 0
    while i + j != elements:
        if i == len(arrA):
            merged_arr[i + j] = arrB[j]
            j += 1
        elif j == len(arrB):
            merged_arr[i + j] = arrA[i]
            i += 1
        elif arrA[i] > arrB[j]:
            merged_arr[i + j] = arrB[j]
            j += 1
        else:
            merged_arr[i + j] = arrA[i]
            i += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) in (0, 1):
        return arr
    else:
        midpoint = len(arr) // 2
        return merge(merge_sort(arr[0:midpoint]),
                     merge_sort(arr[midpoint:len(arr)]))


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):

    start2 = mid + 1

    if arr[mid] <= arr[start2]:
        return arr
    else:
        while start <= mid and start2 <= end:
            if arr[start] <= arr[start2]:
                start += 1
            else:
                start2_value = arr[start2]
                for n in range(start2 - 1, start - 1, -1):
                    arr[n+1] = arr[n]
                arr[start] = start2_value
                start += 1
                mid += 1
                start2 += 1


def merge_sort_in_place(arr, left, right):
    if right - left in (-1, 0):
        return arr
    else:
        midpoint = ((right - left) // 2) + left
        merge_sort_in_place(arr, left, midpoint)
        merge_sort_in_place(arr, midpoint + 1, right)
        return merge_in_place(arr, left, midpoint, right)
