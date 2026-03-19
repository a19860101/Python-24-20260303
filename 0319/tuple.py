# tuple
# 不可變
# 建立
t1 = ('apple', 'banana', 'cherry', 'banana','banana')

# print(t1)
# print(type(t1))

# t2 = tuple([1,2,3,4])
# print(t2)

# t3 = ()
# t4 = tuple()
# print(type(t4))

t5 = (1,)
# print(t5)
# print(type(t5))

# 解構賦值 unpack

size = (1024, 768, 32)
# w = size[0]
# h = size[1]
# d = size[2]

w, h, d = size
# print(w, h, d)

print(t1.index('banana'))
print(t1.count('banana'))
print(len(t1))

# q = t1 + size
t1 = t1 + size
print(t1)

