# 常用字串方法

s = 'hElLo World World'
# 字串大小寫
# 每個單字的首字大寫
print(s.title())
# 轉大寫
print(s.upper())
# 轉小寫
print(s.lower())
# 首字大寫
print(s.capitalize())

#
# print(s.find('H'))
# print(s.find('E'))
print(s.find('o'))
# print(s.find('World'))
print(s.rfind('o'))

print(s.replace('World', 'python'))
print(s.replace('world', 'python'))
