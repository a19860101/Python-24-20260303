# f-string

name = 'John'
n = 25

# print('hello ' + name)
# print(f'Hello {name}! 您是第{n}位訪客')
# print('Hello '+name+'! 您是第' + str(n) +'位訪客')

pi = 3.1415926
# 指定小數位數
print(f'{pi:.2f}')

s = 0.3687
# 轉換百分比
print(f'{s:.2%}')

money = 29600
print(f'{money:,}')

idn = 6
print(f'{idn:05}')