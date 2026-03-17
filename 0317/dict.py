# 字典 Dictionary

user = {
    'name': 'John',
    'age': 21,
    'mail': 'john@gmail.com'
}

# print(user)
# print(user['name'])
# print(user['age'])
# print(user['mail'])

print(user.get('name', '找不到資料'))
print(user.get('hobby', '找不到資料'))
