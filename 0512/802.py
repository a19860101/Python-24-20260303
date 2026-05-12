# 字串轉ASCII
# ord()

s = input()
# s = 'Kingdom'
total = 0
for i in s:
    # print(f'ASCII code for \'{i}\' is {ord(i)}')
    # print(f'ASCII code for "{i}" is {ord(i)}')
    print(f"ASCII code for '{i}' is {ord(i)}")
    # total = total + ord(i)
    total += ord(i)
print(total)
