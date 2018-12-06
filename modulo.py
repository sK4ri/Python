number = 999
modNum = []

while len(modNum) < 25:
    if number % 7 == 0 or number % 9 == 0:
        modNum.append(number)
        number -= 1
    else:
        number -= 1

modNum.sort()

for elem in modNum:
    print(elem)
