
a = list(range(1, 10, 2))
b = map(str, a)
c = list(b)
print(a, b, c, sep='\n')

a = list(map(str, list(range(1, 10, 2))))
print(a)