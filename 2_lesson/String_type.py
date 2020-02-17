# Task 13: Determining the String Type
user_input = input('Give me some input: ')

if user_input.isalpha():
    print('Letters Only')
elif user_input.isnumeric():
    print('Numeric')
else:
    print('Mixed')