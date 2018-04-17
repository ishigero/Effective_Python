# coding: utf-8

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

s = [x**2 for x in nums]
print(s)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

ng = list(map(lambda x: x**2, nums))
print(ng)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_nums = [x**2 for x in nums if x % 2 == 0]
print(even_nums)
# [4, 16, 36, 64, 100]

ng_even_nums = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(ng_even_nums)
# [4, 16, 36, 64, 100]

# for dictionary
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
print(rank_dict)
# {1: 'ghost', 2: 'habanero', 3: 'cayenne'}

chile_len_set = {len(name) for name in rank_dict.values()}
print(chile_len_set)
# {8, 5, 7}