# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    middle = ((end - start) // 2) + start
    if end == -1:
        return -1
    elif target is arr[middle]:
        return middle
    elif end is start:
        return -1
    elif target > arr[middle]:
        return binary_search(arr, target, middle, end)
    else:
        return binary_search(arr, target, start, middle)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def bin_search_helper(arr, target, start, end, comparison):
    middle = ((end - start) // 2) + start
    if end == -1:
        return -1
    elif end - start == 1:
        if target is arr[start]:
            return start
        elif target is arr[end]:
            return end
        else:
            return -1
    elif target is arr[middle]:
        return middle
    elif start is end:
        return -1
    elif comparison(target, arr[middle]):
        return bin_search_helper(arr, target, middle, end, comparison)
    else:
        return bin_search_helper(arr, target, start, middle, comparison)


def agnostic_binary_search(arr, target):
    first = arr[0]
    last = arr[-1]
    end = len(arr) - 1

    if last > first:
        return bin_search_helper(arr, target, 0, end, lambda x, y: x > y)
    else:
        return bin_search_helper(arr, target, 0, end, lambda x, y: x < y)
