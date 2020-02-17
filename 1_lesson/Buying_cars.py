# Task 3: Buying cars
# Prices
mercedes    = 150
rolls_royce = '400'
# Enter the info about the cost of extra equipment
extra_cost = int(input('Please enter the price of extra equipment: '))
# Calculation
two_mercedes    = mercedes * 2
rolls_mercedes  = mercedes + int(rolls_royce)
two_rolls       = int(rolls_royce) * 2 + 2 * extra_cost
mercedes_extra  = mercedes + extra_cost
# List of information
print('Price for two Mercedes is', two_mercedes, 'thousand USD.')
print('Price for Mercedes and Rolls-Royce is', rolls_mercedes , 'thousand USD.')
print('Price for two Rolls-Royce with extra equipment is', two_rolls , 'thousand USD.')
print('Price for two Mercedes with extra equipment', mercedes_extra , 'thousand USD.')