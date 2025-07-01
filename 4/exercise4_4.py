'''   
    # base case
    if start > end:
        return None
      # recursive
    if item < array[mid]:
        return binary_search(array, item, start, mid - 1)
    else:
        return binary_search(array, item, mid + 1, end)
'''
