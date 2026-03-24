import math
n = float(input('n'))
s = float(input('s'))

area = (n * math.pow(s,2)) / (4 * math.tan(math.pi/n))

print(f'area = {area:.4f}')