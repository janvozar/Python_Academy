# Task 5: String operations
# Save name
name = input("Enter name: ")
# Print name
print("Saving" + " '" + name + "' " + "into name... ")
# Save surname
surname = input("Enter surname: ")
# Print surname
print("Saving" + " '" + surname + "' " + "into surname... ")
# Create and print variable full_name
full_name = name + " " + surname
print("Full name: " + full_name)
# Create and print variable name_length
name_length = len(full_name)
print(name_length)
# Print bounded variable full_name
print("=" * name_length)
print(full_name)
print("=" * name_length)