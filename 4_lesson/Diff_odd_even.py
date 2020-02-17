# Task 25: Odd vs. Even
# 1.
nums = [386, 462, 47, 418, 907, 344, 236, 375, 823,
        566, 597, 978, 328, 615, 953, 345, 399, 162,
        758, 219, 918, 237, 412, 566, 826, 248, 866,
        950, 626, 949, 687, 217, 815, 67, 104, 58, 512,
        24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
        742, 717, 958,743, 527]
# 2.
odd = 0
even= 0
# 3.
while len(nums) > 0:
    # 4.
    num = nums.pop()
    # 5.
    if num%2==0:
        even = even + num
    # 6.
    else:
        odd = odd + num
# 7.
result = abs(odd - even)
print('The difference is:', result)