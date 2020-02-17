# Task 15: Splitting Numbers
num = input('Please, give me a number: ')
#1
if num == '':
    print('No input provided')
#2
else:
# 3
    mid_point = len(num) // 2
#4
first_half = int(num[:mid_point])
second_half = int(num[mid_point:])
#5
if first_half % 2 == 0 and second_half % 2 == 0:
    print('Success')
elif first_half % 2 == 0:
    print('First')
elif second_half % 2 == 0:
    print('Second')
else:
    print('Neither')