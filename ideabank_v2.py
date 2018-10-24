import sys

if sys.argv[1] == '--list' :
    with open('ideabank_v2.txt') as f :
        print(f.read())
else:    
    file = open('ideabank.txt', 'a')
    askIdea.append(input('What is your new idea? '))
    file.write(str(askIdea))
    file.close()
    with open('ideabank.txt') as f :
        print(f.read())