import sys
import csv

f = open(sys.argv[1], 'r')
aList = list(csv.reader(f))
f.close()

sList = []

i = 0
for char in range(len(aList[i])) :
    sortChar = sorted(aList[i])
    sList.append(sortChar)
    i += 1

print('Imported list: ', *aList, '\n')
print('Sorted list: ', *sList)