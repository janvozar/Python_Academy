# Task 16: Password check 1
password = input('Please enter the password: ')
if password[0] in 'aefqz':
    print('Welcome!')
else:
    print('The input does not match')