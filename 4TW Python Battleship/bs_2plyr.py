def shooting(grid, row, column, life):
    z = 0
    i = 0 
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
                        life -= 1
                i += 1
        z += 1
    return life

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
    life = length
    return life


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


#ITT KEZDODIK-************-----------------------**************x*#*#x---x#*#*
row = int(input('Hány soros táblát szertnél? \n'))
column = int(input('Hány oszlopos táblát szeretnél? \n'))


#terkepek
#P1
grid1 = [0] * row
grid_boat1 = [0] * row
i = 0
for i in range(row):
    grid_boat1[i] = [0] * column
#P2
grid2 = [0] * row
grid_boat2 = [0] * row
i = 0
for i in range(row):
    grid_boat2[i] = [0] * column
##########################################

#function hajo elhelyezesm elet

#P1
print("Első játékos:")
life1 = ship_placement(grid_boat1, int(input("Hajó kezdősora? \n")), int(input("Hajó kezdőszlopa? \n")), int(input("Hajó iránya? \n")), int(input("Hajó hossza? \n")))

#P2
print("Második játékos:")
life2 = ship_placement(grid_boat2, int(input("Hajó kezdősora? \n")), int(input("Hajó kezdőszlopa? \n")), int(input("Hajó iránya? \n")), int(input("Hajó hossza? \n")))

#######################################x



turn = 5

#print(grid_boat)

#boat printeles

#P1
z = 0
for x in range(len(grid_boat1)):
    i = 0
    for y in range(len(grid_boat1[i])):
        print(grid_boat1[z][i], end = " ")
        i += 1
    z += 1
    print()

#P2
z = 0
for x in range(len(grid_boat2)):
    i = 0
    for y in range(len(grid_boat2[i])):
        print(grid_boat2[z][i], end = " ")
        i += 1
    z += 1
    print()
#####################


while life1 > 0 and life2 > 0 and turn > 0:
    
    print()

    #function shooting

#P1
    life2 = shooting(grid_boat1, int(input("Lövés sora? \n")), int(input("Lövés oszopa? \n")), life1)
    
#P2
    life1 = shooting(grid_boat2, int(input("Lövés sora? \n")), int(input("Lövés oszopa? \n")), life2)    

    print("1. játékos élete: ", life1)
    print("2. játékos élete: ", life2)    
    print("Hátralévő körök: ", turn)
    

    #fogofwar akcio utan
    print()
    print("1. játékos: ")
    fogofwar(grid_boat1)
    print()
    print("2. játékos: ")
    fogofwar(grid_boat2)
    
    ############################

    turn -= 1


print("Játék vége!")