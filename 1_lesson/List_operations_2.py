#Results from previous lesson
candidates = ['Agnes', 'Agnes', 'Agnes']
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire', 'Agnes', 'Agnes', 'Agnes']
# Interval 2-5
print('In interval from 2 to 5 there are: ' +  str(employees[2:6]))
print('Each 3rd member: ' + str(employees[::3]))
# Save index
Jacob_index = employees.index('Jacob')
# Jacob index
print('Jacob is at index: ' + str(Jacob_index))
# Find out number of name Agnes
agnes_number = employees.count('Agnes')
# Number of name Agnes
print('Number of name Agnes in list: ' + str(agnes_number))