# Task 8: List operations 1
# Results from previous task
candidates = ['Bruno', 'Agnes']
employees = ['František', 'Bruno', 'Ann', 'Jacob', 'Claire']
# Remove name candidates
candidates.remove('Bruno')
# Print remaining candidates
print('Bruno removed from candidates: ' + str(candidates))
# Repeat element
candidates = candidates * 3
# Print repeating element in the list candidates
print('Repeating elementt Agnes from the list candidates: ' + str(candidates))
# Join lists
employees = employees + candidates
# Print joined lists
print('Joined candidates and employees: ' + str(employees))
# Index 2
print('On index 2 is: ' + employees[2])
# Find out last index and assign to a variable
last_index = len(employees) - 1
# Last index
print('On ' + str(last_index) + " index is: " + employees[last_index])