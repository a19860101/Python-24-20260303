#set 集合
# 無序、唯一

s1 = {'apple','banana','orange','banana','orange'}

print(s1)
# print(type(s1))

# li1 = ['台北市','台北市','台北市','台北市','新北勢','新北勢','新北勢','新北勢','桃園市','桃園市']
# li1 = set(li1)
# li1 = list(li1)
# li1 = list(set(li1))

# print(li1)

# l1 = set()
# print(type(l1))

# s1.add('pineapple')

# s1.remove('pineapple')
# s1.discard('pineapple')

# s1.clear()
# print(s1)

a = {1,2,3}
b = {3,4,5}

# 聯集
print(a.union(b))
print(a | b)
# 交集
print(a.intersection(b))
print(a & b)
# 差集
print(a.difference(b))
print(a - b)
print(b.difference(a))
print(b - a)
