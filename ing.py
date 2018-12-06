import sys

# testwords: test game lie tip play

wordsNum = len(sys.argv)
i = 1
argWord = ()
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

while i < wordsNum:
    argWord = sys.argv[i]
    if argWord[-2:] == 'ie':
        argWord = argWord[:-2]
        print(argWord + ('ying'), sep='')
        i += 1

    elif argWord[-1] == 'e':
        argWord = argWord[:-1]
        print(argWord + ('ing'), sep='')
        i += 1

    elif argWord[-3] not in vowels and argWord[-2] in vowels and argWord[-1] not in vowels:
        if argWord[-1] == 'y':
            print(argWord + ('ing'), sep='')
            i += 1
        else:
            argWord = argWord + argWord[-1]
            print(argWord + ('ing'), sep='')
            i += 1

    else:
        print(argWord + ('ing'), sep='')
        i += 1
