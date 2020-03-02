# Task 47: Lanagram

def all_anagrams(words):

    if words:

        result = True
        seq= sorted(words.pop())
        for word in words:
            if sorted(word) != seq:
                result = False

    else:

        result = False

    return result

words = ['ship','hips','name']
all_anagrams(words)