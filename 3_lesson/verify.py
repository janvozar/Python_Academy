# Password check 2
# our dictionary with data
data = {
'user1': 'password1',
'Mark': '1234',
'Danny': 'qwert',
}

# we want to ask user for username and password
username    = input('Please enter the username: ')
password    = input('Please enter the password: ')

# two conditions for evaluating the inputs
if data.get(username) != password:
    print('Password or username is wrong')

elif data.get(username) == password:
    print('Permission granted')