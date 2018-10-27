arab_num = 0

def inputNumber(arab) :
  while True :
    try :
        userInput = int(input('Give a number between 0 - 4000: \n'))
        if 0 <= userInput <= 4000 :
            return userInput
            break             
        else : 
            print('Enter a valid number!')
            continue          
    except ValueError :
       print('Enter a number!')
       continue
    else:
       return userInput 
       break 

arab_num = inputNumber(arab_num)

num_length = len(arab_num)

print(num_length)

if num length = 1 :
    for num in range(num_length) :
        if arab_num[0] =  :
            print ('-')
        elif arab_num[0] = 1 :
            print('I')
        elif arab_num[0] = 2 :
            print ('II')
        elif arab_num[0] = 3 :
            print ('III')
        elif arab_num[0] = 4 :
            print ('IV')
        elif arab_num[0] = 5 :
            print ('V')
        elif arab_num[0] = 6 :
            print ('VI')
        elif arab_num[0] = 7 :
            print ('VII')
        elif arab_num[0] = 8 :
            print ('VIII')
        elif arab_num[0] = 9 :
            print ('IX')
        





print('The arab number is: ', arab_num)
print('The roman number is: ', roman_num)