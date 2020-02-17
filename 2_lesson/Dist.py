# Task 17: Distance between 2 points [H]
import math

A = [0,0]
B = [0,0]

A[0] = abs(int(input('Point A, X Coordinate: ')))
A[1] = abs(int(input('Point A, Y Coordinate: ')))
B[0] = abs(int(input('Point B, X Coordinate: ')))
B[1] = abs(int(input('Point B, Y Coordinate: ')))
print("Your inputs have been changed to absolute values.")

a = round(A[0] - B[0], 2)
b = round(A[1] - B[1], 2)
result = round(math.sqrt(a**2 + b**2),2)

print(result)