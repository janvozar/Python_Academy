# Task 39: Min & Max
# function find
def my_find(seq, item):
    for i, obj in enumerate(seq):
        if obj == item:
            return i
    return -1