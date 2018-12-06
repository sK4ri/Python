import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
i = 0

if a > b:
    i = a
else:
    i = b

while i > 0:
    if a % i == 0 and b % i == 0:
        print('The greatest common divisor for these numers is: ', i)
        break
    else:
        i -= 1
