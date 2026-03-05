# 常用字串方法

s = 'hElLo World World'
# 字串大小寫
# 每個單字的首字大寫
# print(s.title())
# 轉大寫
# print(s.upper())
# 轉小寫
# print(s.lower())
# 首字大寫
# print(s.capitalize())

#
# find()
# 尋找。若有找到回傳該文字存在的索引值
# print(s.find('H'))
# print(s.find('E'))
# print(s.find('o'))
# print(s.find('World'))
# 由右側尋找。若有找到回傳該文字存在的索引值
# print(s.rfind('o'))

# replace()
# 取代文字
# print(s.replace('World', 'python'))
# print(s.replace('world', 'python'))


# 計算
# count()
print(s.count('o'))
print(s.count('a'))
print(s.count('World'))

# len()
print(len(s))
