numbersList = []

while True:
    number = input('Enter the number (press x to finish): ')
    if number != 'x':
        numbersList.append(int(number))
    else:
        break

print(numbersList)


def sort_number(numbersList):
    n = len(numbersList)
    i = 1
    while i < n:
        j = 0
        while j <= n - 2:
            if numbersList[j] > numbersList[j + 1]:
                temp = numbersList[j + 1]
                numbersList[j + 1] = numbersList[j]
                numbersList[j] = temp
                j += 1
            else:
                j += 1
        else:
            i += 1
    else:
        print(numbersList)


sort_number(numbersList)
