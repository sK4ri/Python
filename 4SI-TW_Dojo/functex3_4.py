# def rec_funct(a):
#     try:
#         factorial = 1
#         while a > 0:
#             factorial *= a
#             a -= 1
#         return factorial
#     except TypeError:
#         return None

# print(rec_funct(4))


def factorial(n):
    ni = int(n)

    if ni != n or ni <= 0:
        raise ValueError("%s is not a positive integer." % n)

    if ni == 1:
        return 1

    return ni * factorial(ni - 1)

print(factorial(4))