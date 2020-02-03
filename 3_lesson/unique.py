str1 = 'New York'
str2 = 'Yorkshire'
# Difference
unique_str1 = set(str1) - set(str2)
unique_str2 = set(str2) - set(str1)
print('Unique to str1:', list(unique_str1))
print('Unique to str1:', list(unique_str2))