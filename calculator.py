while True:
    a = (input('Enter a number (or letter to exit): '))
    if str.isalpha(a):
        break

    operation = input('Enter an operation: ')
    b = (input('Enter another number: '))

    if operation == '+':
        print('Result: ', int(a) + int(b), '\n')
    if operation == '-':
        print('Result: ', int(a) - int(b), '\n')
    if operation == '*':
        print('Result: ', int(a) * int(b), '\n')
    if operation == '/':
        print('Result:', int(a) / int(b), '\n')
