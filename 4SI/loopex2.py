# total = 0
# for number in range(1, 10 + 1):
#     total += number

# print(total)

# ##############

# print(sum(range(1, 10 + 1)))

# ############
# factorial = 1
# num = int(input("Type in a number:\n"))

# for i in range(1, num + 1):
#     factorial *= i
# print(factorial)

##############
# sum = 0
# prd = 1

# for i in range(1, 10 + 1):
#     x = float(input("Type in the %d. number: " % i))
#     sum += x
#     prd *= x 

# avg = sum/10

# print("Sum = %g\nAverage = %g\nProduct = %g" % (sum, avg, prd))

sum = 0
prd = 1
lst = []

for i in range(10):
    x = float(input("Type in the %d. number: " % (i + 1)))
    lst.append(x)

for j in lst:
    sum += j
    prd *= j

avg = sum/10

print("Sum = %g\nAverage = %g\nProduct = %g" % (sum, avg, prd))

# itt is rossz volt a példa megoldás
