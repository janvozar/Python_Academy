# Task 26: Echo
sentence = 'I do not want to work today'
num_repeat = 3

words = sentence.split()

result = ''

#while words:
#    # 1.
#    word = " " + words.pop(0)
#    # 2.
#    word = word * num_repeat
#    # 3.
#    result = result + word
## 4.
#print(result.lstrip())

while words:
    result = result + (" " + words.pop(0)) * num_repeat
print(result.strip())
