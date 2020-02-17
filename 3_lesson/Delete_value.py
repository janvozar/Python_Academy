# Task 18: Delete value
# Let's define a new dictionary
my_new_dict = {
    'm': 12345,
    'n': 32145,
    'o': 54321,
    'p': 23232,
    'q': 43210,
    'r': 13579
    }
# we want to get the highest value in keys
# and also print it
maximal_value_of_key = max(my_new_dict.keys())
print('The maximal value has the key: ' + maximal_value_of_key)

# the next step is to delete the key if its value is greater than 50000
if max(my_new_dict.values()) > my_new_dict[maximal_value_of_key]:
    del my_new_dict[maximal_value_of_key]

# finally what is the current form of our dictionary?
print(my_new_dict)