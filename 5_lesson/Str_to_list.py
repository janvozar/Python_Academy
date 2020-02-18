# Task 30: String to list

inpt = input('Hello, please write your numbers and press enter to confirm: ')
nums = inpt.split(',')
result = []

for num in nums:
    num = int(num.strip())
    result.append(num)

print('List:', result)