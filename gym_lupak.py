questions = ['are you over 14?', 'Wanna use the sauna?', 'Are you a student?', 'Are you a Male?']

while True:
    o14 = input(questions[0])
    while o14 == 'Yes' or o14 == 'No':
        if o14 == 'Yes':
            sauna = input(questions[1])
            while sauna == 'Yes' or sauna == 'No':
                if sauna == 'Yes':
                    print('final:', 1500)
                    break
                else:
                    student = input(questions[2])
                    while student == 'Yes' or student == 'No':
                        if student == 'Yes':
                            print('final:', 300)
                            break
                        else:
                            men_women = input(questions[3])
                            while men_women == 'Yes' or men_women == 'No':
                                if men_women == 'Yes':
                                    print('final:', 750)
                                    break
                                else:
                                    print('final:', 500)
                                    break
                        break
                    break
            break
        else:
            print('Too young!')
            break
    else:
        print('try again hülyegyerek')


#         answers lista????

#         questions = ['Are you over 14?\n','Want to use sauna?\n','Are you a student?\n','Are you Male?\n']
# answers = []

# def question() :
#     answer = input(questions[i])
#     if answer == 'yes' :
#         answers.append('1')
#     elif answer == 'no' :
#         answers.append('0')
#     else :
#         print('Please type yes or no')

# for i in range(len(questions)) :
#     question()
