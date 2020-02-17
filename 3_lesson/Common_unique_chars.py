# Task 21: Common & Unique
# our inputs
string01 = 'Bratislava'
string02 = 'Budapest'

# our operations
common = set(string01) & set(string02)
unique = set(string01) - set(string02)

# print section
print('Common characters: ' + str(Common))
print('Unique characters: ' + str(Unique))