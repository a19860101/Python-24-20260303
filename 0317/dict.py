# 字典 Dictionary

user = {
    'name': 'John',
    'age': 21,
    'mail': 'john@gmail.com'
}

# user2 = {}
# user3 = dict()
# user4 = dict(name='John', age=22, mail='')

# print(user)

# print(user)
# print(user['name'])
# print(user['age'])
# print(user['mail'])

# print(user.get('name', '找不到資料'))
# print(user.get('hobby', '找不到資料'))

#
# 取得所有值
# print(user.values())
# 取得所有鍵
# print(user.keys())
# 取得所有鍵、值
print(user.items())

for v in user.values():
    print(v)

for k in user.keys():
    print(k)

for k, v in user.items():
    print(f'{k}: {v}')

