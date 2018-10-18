# row = input('row')
# colum = input('column')

x = 5
y = 5
a = [0] * x
for i in range(x):
    a[i] = 'o' * y
    p = 0
for x in range(len(a)):
    i = 0
    for z in range(len(a[i])):
        print(a[p][i], end=' ')
        i += 1
    p += 1
    print()