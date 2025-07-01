def max_number(array):
    if not array:
        return None 
    if len(array) == 1:
        return array[0]
    middle = len(array) // 2
    left_max = max_number(array[:middle])
    right_max = max_number(array[middle:])
    if left_max > right_max: 
        return left_max
    else:
        return right_max
