#
# t1 = ()
# t2 = ()
#
# print('Create tuple1:')
# while True:
#     n = int(input())
#     if n == -9999:
#         break
#     t1 += (n,)
# print('Create tuple2:')
# while True:
#     n = int(input())
#     if n == -9999:
#         break
#     t2 += (n,)
#
# print(f'Combined tuple before sorting: {t1 + t2}')
# print(f'Combined tuple before sorting: {sorted(t1 + t2)}')


t1 = []
t2 = []

print('Create tuple1:')
while True:
    n = int(input())
    if n == -9999:
        break
    t1.append(n)
print('Create tuple2:')
while True:
    n = int(input())
    if n == -9999:
        break
    t2.append(n)

# print([1,2,3] + [4,5,6])
# a = [1,2,3] + [9,5,6]
# a.sort()
# print(a)
result = t1 + t2
result.sort()

print(f'Combined tuple before sorting: {tuple(t1 + t2)}')
print(f'Combined tuple before sorting: {result}')