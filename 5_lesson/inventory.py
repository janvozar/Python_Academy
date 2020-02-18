data = [['ID','Name', 'Price', 'Amount', 'Supplier'],
        ['321','Ibalgin', 40.50, 2841, 'Zentiva'],
        ['534','Paralen', 19.90, 3229, 'Zentiva'],
        ['327','Smecta', 68.00, 2709, 'Sipsen'],
        ['242','Uniclophen', 76.00, 476, 'UNIMED']]

# Code tasks:
# What is the total price of our inventory?
# What is the total amount of items in our warehouse?
# How many items do we have from the company called Zentiva?
# Let's transfer the above table into a dictionary of dictionaries. How would we do that?

# 1. Total price of our inventory
total_price = 0
for row in data[1:]:
    total_price = total_price + row[2] * row[3]
print("The total price of our inventory: ", total_price)
# 2. Total amount of items in our warehouse
num_items = 0
for row in data[1:]:
    num_items = num_items + row[3]
print("The total amount of items in our warehouse: ", num_items)
# 3. Items from Zentiva
num_items = 0
for row in data[1:]:
    if row[4] == 'Zentiva':
        num_items = num_items + row[3]
print("The amount of Zentiva produts: ", num_items)
# 4. Table into a dictionary of dictionaries.
d = {}
header = data[0][1:]
for row in data[1:]:
    id = row[0]
    d[id] = {}
    for i,item in enumerate(row[1:]):
        key = header[i]
        d[id].update({key: item})
print("Database dictionary: ", d)