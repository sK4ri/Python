# from random import randint

# numbers = []

# for i in range(10):
#     numbers.append(randint(1, 100))


# def sqr_calc(numbers):
#     for num in range(len(numbers)):
#         numbers[num] = numbers[num] ** 2

# sqr_calc(numbers)

# print("Sum:", sum(numbers))


even_numbers = {2, 4, 6, 8, 10}
big_numbers = {6, 7, 8, 9, 10}

# subtraction: big numbers which are not even
print(big_numbers - even_numbers)

# union: numbers which are big or even
print(big_numbers | even_numbers)

# intersection: numbers which are big and even
print(big_numbers & even_numbers)

# numbers which are big or even but not both
print(big_numbers ^ even_numbers)