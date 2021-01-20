some_list = range(1, 1000, 7)

some_list = list(map(lambda x: x * 2, some_list))
itr = iter(some_list)

print(next(itr))
print(next(itr))
print(next(itr))