import random

numAttacker = 0
numDefender = 0

while True :
    numAttacker = int(input('How many attackers will you use? (1 - 3) '))
    if 1 <= numAttacker <= 3 :
        break
    else :
        print('Try again!')

while True :        
    numDefender = int(input('How many defenders will you use? (1 - 2) '))
    if 1 <= numDefender <= 2 :
        break
    else :
        print('Try again!')

listAttacker = []
listDefender = []


for i in range(numAttacker) :
    listAttacker.append(random.randrange(1, 6))
for i in range(numDefender) :
    listDefender.append(random.randrange(1, 6))

listAttacker.sort(reverse = True)
listDefender.sort(reverse = True)

attackerLost = 0
defenderLost = 0

i = 0

while i < len(listDefender) :
    if listAttacker[i] <= listDefender [i] :
        attackerLost += 1
        i += 1
    else :
        defenderLost += 1
        i += 1

if attackerLost > 1 :
    attackerUnit = 'units'
else :
    attackerUnit = 'unit'
if defenderLost > 1 :
    defenderUnit = 'units'
else :
    defenderUnit = 'unit'


print('Dice:')
print('  Attacker: ', listAttacker)
print('  Defender: ', listDefender, '\n')
print('Outcome:')
print('  Attacker: Lost %i %s' % (attackerLost, attackerUnit))
print('  Defender: Lost %i %s' % (defenderLost, defenderUnit))