n = int(input())

for i in range(n):
    # print(i)
    ip = input()
    ip_list = [float(i) for i in ip.split()]
    ans = max(ip_list) - min(ip_list)
    print(f'{ans:.2f}')
# ip = input()

# print(ip.split())

# print([float(i) for i in ip.split()])

# ip_list = [float(i) for i in ip.split()]
# print(max(ip_list) - min(ip_list))

# ans = max(ip_list) - min(ip_list)
# print(f'{ans:.2f}')