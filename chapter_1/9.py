# coding: utf-8
#generator
words = ['hoge', 'fug', 'oo', 'i']
it = (len(word) for word in words)
print(it)
print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

c = ((x, x*2) for x in it)
print(c)
print(next(c))
print(next(c))

# <generator object <genexpr> at 0x7fa8dda48f10>
# 4
# <generator object <genexpr> at 0x7fa8dda48048>
# (3, 6)
# (2, 4)