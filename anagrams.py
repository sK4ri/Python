import sys
import csv

# create list of anagram words from file:
f = open(sys.argv[1], 'r')
aList = list(csv.reader(f))
f.close()

# create list of anagram words' sorted letters:
sList = []
for elem in aList:
    for char in elem:
        sList.append(sorted(char))

# check if there are matching between sorted words:
i = 0
j = 1
while j < len(aList):
    if sList[i] == sList[j]:
        print(*aList[i], '\n', *aList[j], '\n', sep='')
        i += 1
        j = i + 1
    elif sList[i] != sList[j]:
        j += 1
    else:
        break
