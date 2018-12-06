import math

coordinates = []
i = 0

# number input validation :


def inputNumber(coordnate):
    while True:
        try:
            userInput = int(input('Input coordinate number (-100 - 100): \n'))
            if -100 <= userInput <= 100:
                coordinates.append(userInput)
            else:
                print('Enter a valid number!')
                continue
        except ValueError:
            print('Enter a number!')
            continue
        else:
            return userInput
            break

# distance between vertices :


def distance(x1, y1, x2, y2):
    length = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return length


# main // input from user :
while i < 6:
    inputNumber(coordinates)
    i += 1

print('Coordinates: ', *coordinates)

# math
side1 = distance(
    coordinates[0],
    coordinates[1],
    coordinates[2],
    coordinates[3])
side2 = distance(
    coordinates[0],
    coordinates[1],
    coordinates[4],
    coordinates[5])
side3 = distance(
    coordinates[2],
    coordinates[3],
    coordinates[4],
    coordinates[5])

sp = (side1 + side2 + side3) / 2

area = math.sqrt(sp * (sp - side1) * (sp - side2) * (sp - side3))

print(side1, side2, side3)
print('The area of the triangle is: ', '%.1f' %
      area)  # there is always one decimal point
