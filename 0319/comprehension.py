# 生成式

list1 = [1,2,3,4,5,6,7,8,9]
drinks = ['紅茶','綠茶','美式咖啡','拿鐵']

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
# result = [ data+3.1415926 for data in list1 ]

# result = [data for data in list1 if data > 5]
# result_even = [data for data in list1 if data % 2 == 0]
# result_odd = [data for data in list1 if data % 2 == 1]

# result = [data for data in drinks if data.find('茶')>-1]
result = [data for data in drinks if data.find('茶')==-1]

print(result)