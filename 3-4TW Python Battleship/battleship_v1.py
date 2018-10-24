def shooting(grid, row, column):
    z = 0
    i = 0 
    hit = 0
    for x in range(len(grid)):   
        if row == z:
            for y in range(len(grid[i])):
                if column == i:
                    if grid[z][i] == 0:
                        grid[z][i] = "#"
                        i += 1
                    else:
                        grid[z][i] = "H"
                        i += 1 
                        hit = 1
                i += 1
        z += 1
    return hit

def ship_placement(grid, row, column, direction, length):
    z = 0
    i = 0
    k = 0
    if direction == 1:
        for x in range(len(grid)):
            for y in range(len(grid[i])):
                if row == z and column == i:
                    grid[z][i] = "X"
                    i += 1
                    k += 1
                elif row < z and column == i:
                    while k < length:
                        grid[z][i] = "X"
                        k += 1
                        i += 1
                        break
                else:
                    grid[z][i] = 0
                    i += 1
            i = 0
            z += 1
    elif direction == 0:
        for x in range(len(grid)):  
            i = 0
            if row == z:
                for y in range(len(grid[i])):
                    if column == i:
                        while k < length:
                            grid[z][i] = "X"
                            k += 1
                            i += 1
                    i += 1
                z += 1
            else:
                for y in range(len(grid[i])):
                    i += 1
                z += 1
            print()
    return length

def fogofwar(grid):
    z = 0
    for x in range(len(grid)):
        i = 0
        for y in range(len(grid[i])):
            if grid[z][i] == "#" or grid[z][i] == "H":
                print(grid[z][i], end = " ")
                i += 1
            else:
                print(0, end = " ")
                i += 1
        z += 1
        print()

def print_grid_preview(grid):
    z = 0
    for x in range(len(grid)):
        i = 0
        for y in range(len(grid[i])):
            print(grid[z][i], end = " ")
            i += 1
        z += 1
        print()

#ITT KEZDODIK-************-----------------------**************x*#*#x---x#*#*
row = int(input('Hány soros táblát szertnél? \n'))
column = int(input('Hány oszlopos táblát szeretnél? \n'))
turn = int(input("Hány körös legyen? \n"))

#palyak
import copy
grid1 = [0] * row
i = 0
for i in range(row):
    grid1[i] = [0] * column
grid2 = copy.deepcopy(grid1)

##########################################

#hajo elhelyezes
    #P1
print("Első játékos:")
life1 = ship_placement(grid1, int(input("Hajó kezdősora? \n")), int(input("Hajó kezdőszlopa? \n")), int(input("Hajó iránya? \n")), int(input("Hajó hossza? \n")))

    #P2
print("Második játékos:")
life2 = ship_placement(grid2, int(input("Hajó kezdősora? \n")), int(input("Hajó kezdőszlopa? \n")), int(input("Hajó iránya? \n")), int(input("Hajó hossza? \n")))

print()

#boat printeles
    #P1
print_grid_preview(grid1)
    #P2
print()
print_grid_preview(grid2)

print("##########################################################")

while life1 > 0 and life2 > 0 and turn > 0:   
    print()

#function shooting
    #P1
    print("Első játékos lő: \n")
    life2 = life2 - shooting(grid1, int(input("Lövés sora? \n")), int(input("Lövés oszopa? \n")))
    #P2
    print("Második játékos lő: \n")
    life1 = life1 - shooting(grid2, int(input("Lövés sora? \n")), int(input("Lövés oszopa? \n")))

#állás
    print()
    print("1. játékos élete: ", life1)
    print("2. játékos élete: ", life2)
    print("Hátralévő körök: ", turn)

#fogofwar akcio utan
    print()
    print("1. játékos: ")
    fogofwar(grid1)
    print()
    print("2. játékos: ")
    fogofwar(grid2)

    turn -= 1
    
if life2 == 0 :
    print("1. játékos nyert!")
elif life1 == 0 :
    print("2. játékos nyert!")
elif turn == 0 :    
    print("Játék vége!")