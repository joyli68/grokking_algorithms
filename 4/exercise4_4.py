def binary_search(array, item, start=0, end=None):

    if end is None:
        end = len(array) - 1

    # base case
    if start > end:
        return None

    mid = start + (end - start) // 2

    if array[mid] == item:
        return mid

    # recursive
    if item < array[mid]:
        return binary_search(array, item, start, mid - 1)
    else:
        return binary_search(array, item, mid + 1, end)
