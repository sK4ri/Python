# while True:
#     num = int(input("Type in a number: "))
#     if num == 99:
#         break
#     if num % 2:
#         continue
#     print(num)


#############################

# print("Calculate the given positive numbers average:")
# sum_num = 0
# num_count = 0
# while True:
#     num = int(input("Type in a psitive number(the program terminates to negative number): "))
#     if num < 0:
#         break
#     else:
#         sum_num += num
#         num_count += 1
#         print(sum_num, num_count)
# print(sum_num / num_count)


#############################

menu = """-- Calculator Menu --
0. Quit
1. Add two numbers
2. Subtract two numbers
3. Multiply two numbers
4. Divide two numbers"""

selection = None

while selection != 0:
    print(menu)
    selection = int(input("Select an option: "))

    if selection not in range(5):
        print("Invalid option: %d" % selection)
        continue

    if selection == 0:
        continue

    a = float(input("Please enter the first number: "))
    b = float(input("Please enter the second number: "))

    if selection == 1:
        result = a + b
    elif selection == 2:
        result = a - b
    elif selection == 3:
        result = a * b
    elif selection == 4:
        result = a / b

    print("The result is %g." % result)
