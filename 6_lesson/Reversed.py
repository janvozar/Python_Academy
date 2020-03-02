

def my_reversed(sequence):
    return list(sequence[::-1])

def my_reversed(sequence):
    result = []
    for item in sequence:
        result.insert(0,item)
    return result