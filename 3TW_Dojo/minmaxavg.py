numbers = [-5, 23, 0, "dupa", -9, 12, 99, [2, 44], None, 105, -43]

#Filter the original list to numbers - except list in list
filteredNumbers = []

for elem in numbers :
    try :
        filteredNumbers.append(int(elem))
    except ValueError :
        continue
    except TypeError :
        continue        
print('Numbers: ', filteredNumbers)

#Compute minimum of numbers list
def min_num(filteredNumbers) :
    min = filteredNumbers[0]
    for number in filteredNumbers :
        if number < min :
            min = number
    return min
print('Minimum of numbers: ', min_num(filteredNumbers))

#Compute maximum of numbers list
def max_num(filteredNumbers) :
    max = filteredNumbers[0]
    for number in filteredNumbers :
        if number > max :
            max = number
    return max
print('Maximum of numbers: ', max_num(filteredNumbers))

#Compute average of numbers list
def avg_num(filteredNumbers) :
    avg = 0
    for number in filteredNumbers :
        avg = avg + number
    avg = avg / len(filteredNumbers)
    return avg
print('Average of numbers: ', avg_num(filteredNumbers))