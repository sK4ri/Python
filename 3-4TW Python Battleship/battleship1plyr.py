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
                print(grid[z][i], end=" ")
                i += 1
            else:
                print(0, end=" ")
                i += 1
        z += 1
        print()


# ITT KEZDODIK-************-----------------------**************x*#*#x---x#*#*
row = int(input('How many rows do you want? \n'))
column = int(input('How many column do you want? \n'))


# terkepek
grid = [0] * row
grid_boat = [0] * row
i = 0
for i in range(row):
    grid_boat[i] = [0] * column
##########################################

# function hajo elhelyezesm elet
life = ship_placement(
    grid_boat, int(
        input("Sor")), int(
            input("Oszlop")), int(
                input("Irány")), int(
                    input("Hossz")))

# x


turn = 5

print(grid_boat)

# boat printeles
z = 0
for x in range(len(grid_boat)):
    i = 0
    for y in range(len(grid_boat[i])):
        print(grid_boat[z][i], end=" ")
        i += 1
    z += 1
    print()
#####################


while life > 0 and turn > 0:

    print()

    # function shooting
    life = shooting(
        grid_boat, int(
            input("lövés sor:")), int(
            input("lövés oszop:")), life)
    # JÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓ

    print(life)
    print("Turns left:", turn)
    print(grid_boat)

    # fogofwar akco utan
    print()
    fogofwar(grid_boat)
    ############################

    turn -= 1


print("game over")
