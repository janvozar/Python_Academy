# Conversion rates
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26
# Amount of units for conversion.
kg_amount = 80
km_amount = 54
l_amount = 3
# Conversion calculations
kg_result = kg_lb * kg_amount
km_result  = km_mile * km_amount
l_result  = l_gal * l_amount
# Final answers
print(kg_amount, 'kg is', kg_result , 'lb')
print(km_amount, 'kg is', km_result , 'mil')
print(l_amount, 'l is', l_result , 'gal')