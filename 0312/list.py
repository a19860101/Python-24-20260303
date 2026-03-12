l1 = ['apple', 'banana', 'cat','dog','elephant','fork','cat']
# print(l1)
# print(l1[0])
# print(l1[1])
# print(l1[2])
# list切片
# list[start: end: step]
# print(l1[0:3])
# print(l1[:4])
# print(l1[4:])
# print(l1[::-1])
# print(l1[::2])

# 遍歷
# for x in l1:
#     print(x)

# enumerate
# for x in enumerate(l1):
#     print(x)
#     print(x[0], x[1])

# for idx,data in enumerate(l1):
    # print(idx)
    # print(data)

# list方法
# 新增
# append()
# l1.append('asdf')

# insert()
# l1.insert(1, 'test')

# extend()
# l1.extend(['test', 'test2', 'test3'])

# 刪除
# l1.remove('cat')

# l1.pop()
# l1.pop(2)

# del l1[3]

# l1.clear()

# 查詢
# l1.index('cat')

# print(l1.index('c;l'))
# print(l1.count('apple'))
# print(l1.count('lkjh'))

# print('apple' in l1)
# print('ddd' in l1)

# 排序
# l1.sort()
# l1.sort(reverse=True)
# l1.reverse()

l2 = sorted(l1)
print(l1)
print(l2)