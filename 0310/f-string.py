# f-string

name = 'John'
n = 178

# print('hello ' + name)
# print(f'Hello {name}! 您是第{n}位訪客')
# print('Hello '+name+'! 您是第' + str(n) +'位訪客')

pi = 3.1415926
# 指定小數位數
# print(f'{pi:.2f}')

s = 0.3687
# 轉換百分比
# print(f'{s:.2%}')

money = 29600
# print(f'{money:,}')

# print(f'{name:10}')

idn = 6
# print(f'{idn:05}')
# 對齊
# < 靠左
# > 靠右
# ^ 置中
# print(f'{name:_^20}')
# print(f'{name:*>20}')
# print(f'{name:<20}')

# 進位轉換

print(f'{n:b}')
print(f'{n:x}')
print(f'{n:X}')
print(f'{n:#x}')
print(f'{n:#X}')
print(f'{n:o}')


# rgb(8, 144, 35)
r = 250
g = 162
b = 6
print(f'#{r:02X}{g:02X}{b:02X}')