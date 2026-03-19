# 生成式

list1 = [1,2,3,4,5,6,7,8,9]

# 原始寫法
# result = []
#
# for data in list1:
#     x = data ** 2
#     result.append(x)

# 生成式
# result = [data ** 2 for data in list1 ]
# result = [str(data) for data in list1 ]
# result = [float(data) for data in list1 ]
result = [ data+3.1415926 for data in list1 ]


print(result)