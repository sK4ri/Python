userNum = int(input('How many numbers do you want to print out? '))
print('Fibonacci sequence: ')

i = 0
j = 1
k = 0
fib = 0

while i < userNum :
    print (str(i), str(fib).rjust(20), sep=':')  #Whitespaces aren'T dinamic yet!
    fib = j + k
    j = k
    k = fib
    i += 1