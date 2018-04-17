# Your code here!

#generator
print('start index is 0')
colors = ['white', 'blue', 'green', 'red']
for i, color in enumerate(colors):
    print('%d: %s is beautiful' % (i, color))

print('start index is 1') 
colors = ['white', 'blue', 'green', 'red']
for i, color in enumerate(colors, 1):
    print('%d: %s is beautiful' % (i, color))



# start index is 0
# 0: white is beautiful
# 1: blue is beautiful
# 2: green is beautiful
# 3: red is beautiful
# start index is 1
# 1: white is beautiful
# 2: blue is beautiful
# 3: green is beautiful
# 4: red is beautiful