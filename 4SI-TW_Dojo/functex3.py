from math import sqrt


def hypotenuse(a, b):
    try:
        return(sqrt((a**2) + (b**2)))
    except TypeError:
        return None


print(hypotenuse(2.3, 3.4))

print(hypotenuse("3", 4))

print(hypotenuse(3, 5.67))
