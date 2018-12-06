import copy


def shooting(grid, row, column):
    hit = 0
    if grid[row][column] == 0:
        grid[row][column] = "#"
    elif grid[row][column] == "X":
        grid[row][column] = "H"
        hit = 1

    return hit


def ship_placement(grid, row, column, direction, length):
    k = 0
    if direction == 1:
        while k < length:
            grid[row + k][column] = "X"
            k += 1
    elif direction == 0:
        while k < length:
            grid[row][column + k] = "X"
            k += 1
    return length


def fogofwar(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#" or grid[i][j] == "H":
                print(grid[i][j], end=" ")
            else:
                print(0, end=" ")
        print()


def cheatsheet(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#" or grid[i][j] == "H" or grid[i][j] == "X":
                print(grid[i][j], end=" ")
            else:
                print(0, end=" ")
        print()


def print_grid_preview(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=" ")
        print()


def outofgrid(grid, row, column, direction, length):
    if direction == 1:
        if row < 0 or row > len(
                grid) or row + length > len(grid) or column < 0 or column > len(grid[0]):
            allgood = 0
        else:
            allgood = 1
    elif direction == 0:
        if row < 0 or row > len(grid) or column < 0 or column > len(
                grid[0]) or column + length > len(grid[0]):
            allgood = 0
        else:
            allgood = 1
    else:
        allgood = 0
        print("Direction error! 1 is vertical, 0 is horizontal.")
    return allgood


# ITT KEZDODIK-************-----------------------**************x*#*#x---x#*#*
# try:
#     sor = int(input('Hány soros táblát szertnél? \n'))
#     oszlop = int(input('Hány oszlopos táblát szeretnél? \n'))
#     turn = int(input("Hány körös legyen? \n"))
# except ValueError:
#     print("Please enter a valid parameter!\n")
sor = 5
oszlop = 5
turn = 5


# palyak
grid1 = [0] * sor
i = 0
for i in range(sor):
    grid1[i] = [0] * oszlop
grid2 = copy.deepcopy(grid1)

##########################################

# hajo elhelyezes
allgood = 0
while allgood == 0:
        # P1
    print("First player:")
    try:
        rowboat = int(input("Row of ship? \n"))
        columnboat = int(input("Column of ship? \n"))
        direction = int(input("Direction of ship? \n"))
        length = int(input("Length of ship? \n"))
    except ValueError:
        print("Please enter a valid parameter!\n")
        continue
    life1 = ship_placement(grid1, rowboat, columnboat, direction, length)
    allgood = outofgrid(grid1, rowboat, columnboat, direction, length)
    if allgood == 0:
        continue
        # P2
    print("Second player:")
    try:
        rowboat = int(input("Row of ship? \n"))
        columnboat = int(input("Column of ship? \n"))
        direction = int(input("Dircetion of ship? \n"))
        length = int(input("Length of ship? \n"))
    except ValueError:
        print("Please enter a valid parameter!\n")
        continue
    life2 = ship_placement(grid2, rowboat, columnboat, direction, length)
    allgood = outofgrid(grid2, rowboat, columnboat, direction, length)

print()

# boat printeles
# P1
print_grid_preview(grid1)
# P2
print()
print_grid_preview(grid2)

print("##########################################################")

while life1 > 0 and life2 > 0 and turn > 0:
    print()

# function shooting
    allgood = 0
    while allgood == 0:
        # P1
        print("First player shoots:\n")
        try:
            rowboat = int(input("Row of target?\n"))
            columnboat = int(input("Column of target?\n"))
        except ValueError:
            print("Please enter a valid parameter!\n")
            continue
        life2 = life2 - shooting(grid1, rowboat, columnboat)
        allgood = outofgrid(grid1, rowboat, columnboat, 1, 0)
        if allgood == 0:
            continue
        # P2
        print("Second player shoots:\n")
        try:
            rowboat = int(input("Row of target?\n"))
            columnboat = int(input("Column of target?\n"))
        except ValueError:
            print("Please enter a valid parameter!\n")
            continue
        life1 = life1 - shooting(grid2, rowboat, columnboat)
        allgood = outofgrid(grid2, rowboat, columnboat, 1, 0)

# állás
    print()
    print("First players life:", life1)
    print("Second players life:", life2)
    print("Turns left:", turn)

# fogofwar akcio utan
    print()
    print("First player:")
    fogofwar(grid1)
    print()
    print("Second player:")
    fogofwar(grid2)

    print()
    cheatsheet(grid1)
    print()
    cheatsheet(grid2)
    print()
    turn -= 1

if life2 == 0:
    print("First player wins!")
elif life1 == 0:
    print("Second player wins!")
elif turn == 0:
    print("Game fucking over, mate!")
