# Task 22. Difference & All
# our inputs
string01 = 'Bratislava'
string02 = 'Budapest'

# our operations
difference  = set(string01) ^ set(string02)
all         = set(string01) | set(string02)

# print() section
print('Different characters: ' + str(difference))
print('All characters: ' + str(all))