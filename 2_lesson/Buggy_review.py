# Task 14: Find bugs
some_str = input('Hello, please enter anything you want: ')
    if some_str.isupper():
        print('All letters in your input are uppercase')
    elif some_str.islower():
        print('All letters in your input are lowercase')k
    else:
        print('There are both uppercase and lowercase letters')