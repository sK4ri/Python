import sys

if sys.argv[1] == '--list' :
    with open('ideabank.txt') as f :
        print(f.read())

else:    
    file = open('ideabank.txt', 'a')
    ideaNum = sum(1 for line in open('ideabank.txt') if line.rstrip())
    ideaNum = (ideaNum)
    askIdea = input('What is your new idea? ')
    file.write('\n')
    file.write(str(ideaNum))
    file.write('. ')
    file.write(str(askIdea))
    file.close()
    with open('ideabank.txt') as f :
        print(f.read())