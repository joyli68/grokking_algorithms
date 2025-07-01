# 4.2
def count(array):
    if not array:
        return 0
    return 1 + count(array[1:])