# Task 38: Min & Max

def my_min(sequence):
    min = sequence[0]
    for item in sequence[1:]:
        if item < min:
            min = item
    return min


def my_max(sequence):
    max = sequence[0]
    for item in sequence[1:]:
        if item > max:
            max = item
    return max
