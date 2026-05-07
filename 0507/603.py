n = []

for i in range(10):
    q = int(input())
    n.append(q)

n.sort(reverse=True)

print(' '.join(str(i) for i in n[:3]))
