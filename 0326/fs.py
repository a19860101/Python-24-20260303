data = ['apple','banana','mango','peach','pineapple']

with open('0326.txt','w',encoding='utf-8') as f:
    for item in data:
        f.write(item + '\n')
    # f.writelines(data)

# f = open('0326.txt','w',encoding='utf-8')
# for item in data:
#     f.write(item + '\n')
# print(f.closed)

with open('0326.txt','r',encoding='utf-8') as f:
    content = f.read()
    # content = f.readline()
    # content = f.readlines()

print(content)
