# Task 44: Lorem Ipsum

import random

words = {'articles' : ("the", "a", "an"),
        'determiners' : ("another", "this", "every", "many"),
        'subjects' : ("cat", "dog", "man", "woman"),
        'verbs' : ("sang", "ran", "jumped"),
        'adverbs' : ("loudly", "quietly", "well", "badly")}

combinations = [["articles", "subjects", "verbs", "adverbs"],
                ["determiners", "subjects", "verbs"],
                ["determiners", "subjects", "verbs", "adverbs"]]


def lorem_poetry(num_rows):
    rows = []
    for _ in range(num_rows):
        combination = random.choice(combinations)
        row = []
        for category in combination:
            row.append(random.choice(words[category]))
        rows.append(' '.join(row))

    result = '\n'.join(rows)
    print(result)
    return result

poetry = lorem_poetry(5)