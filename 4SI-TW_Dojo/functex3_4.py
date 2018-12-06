def factorial(n):
    ni = int(n)

    if ni != n or ni <= 0:
        raise ValueError("%s is not a positive integer." % n)

    if ni == 1:
        return 1

    return ni * factorial(ni - 1)


print(factorial(4))
