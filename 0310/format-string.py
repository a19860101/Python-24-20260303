# 格式化字串 format

name = 'JOhn'
temp = 20
n=123
# msg = 'hello {} 今天溫度為{}度 您是第{}位訪客'
# msg = 'hello {2} 今天溫度為{1}度 您是第{0}位訪客'
msg = 'hello {a} 今天溫度為{b}度 您是第{c}位訪客'

# print(msg.format(name,temp,123))
print(msg.format( b=temp, c=n, a=name))

print('{:.2f}'.format(3.1415926))
print('{:10}'.format('john'))
print('{:>10}'.format('john'))
print('{:^10}'.format('john'))
print('{:_^10}'.format('john'))
print('{:,}'.format(123123123))
print('{:x}'.format(255))
print('{:b}'.format(255))
print('{:o}'.format(255))

