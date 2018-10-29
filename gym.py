questions = ['Are you over 14?\n','Want to use sauna?\n','Are you a student?\n','Are you Male?\n']

while True :
    q1 = input(questions[0])
    if q1 == 'no' :
        print('You are underage!')
        break
    elif q1 == 'yes' :
        q2 = input(questions[1])        
        if q2 == 'yes' :
            print('Price: 1500HUF')
            break
        elif q2 == 'no' :
            q3 = input(questions[2])            
            if q3 == 'yes' :
                print('Price: 300HUF')
                break
            elif q3 == 'no' :
                q4 = input(questions[3])               
                if q4 == 'yes' :

                    print('Price: 750HUF')
                    break
                elif q4 == 'no' :
                    print('Price: 500HUF')
                    break