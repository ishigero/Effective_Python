# coding: utf-8
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('first four:', nums[:4])
print('last four:', nums[-4:])
print('middle two:', nums[3:-3])

print('1:', nums[:])
print('2:', nums[:5])
print('3:', nums[:-1])
print('4:', nums[4:])
print('5:', nums[-3:])
print('6:', nums[2:5])
print('7:', nums[2:-1])
print('8:', nums[-3:-1])


# first four: [0, 1, 2, 3]
# last four: [7, 8, 9, 10]
# middle two: [3, 4, 5, 6, 7]
# 1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 2: [0, 1, 2, 3, 4]
# 3: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 4: [4, 5, 6, 7, 8, 9, 10]
# 5: [8, 9, 10]
# 6: [2, 3, 4]
# 7: [2, 3, 4, 5, 6, 7, 8, 9]
# 8: [8, 9]