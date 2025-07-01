# 4.1
def recursive_sum(array):
    if not array:
        return 0
    return array[0] + recursive_sum(array[1:])