import copy
import os
os.system('clear')


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


def fog_of_war(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#" or grid[i][j] == "H":
                print(grid[i][j], end=" ")
            else:
                print(0, end=" ")
        print()


def cheat_sheet(grid):
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


def out_of_grid(grid, row, column, direction, length):
    if direction == 1:
        if row < 0 or row > len(
                grid) or row + length > len(grid) or column < 0 or column > len(grid[0]):
            all_good = 0
            print("Please enter valid parameters!\n")
        else:
            all_good = 1
    elif direction == 0:
        if row < 0 or row > len(grid) or column < 0 or column > len(
                grid[0]) or column + length > len(grid[0]):
            all_good = 0
            print("Please enter valid parameters!\n")
        else:
            all_good = 1
    else:
        all_good = 0
        print("Direction error! 1 is vertical, 0 is horizontal.")
    return all_good


def print_all():
    # állás
    print("\nFirst players life:", life1)
    print("Second players life:", life2)
    print("Turns left:", turn)
    # fog_of_war akcio utan
    print("\nFirst player:")
    fog_of_war(grid1)
    print("\nSecond player:")
    fog_of_war(grid2)
    print()
    cheat_sheet(grid1)
    print()
    cheat_sheet(grid2)
    print()

# ITT KEZDODIK-************-----------------------**************x*#*#x---x#*#*
# try:
#     row = int(input('Hány soros táblát szertnél? \n'))
#     column = int(input('Hány oszlopos táblát szeretnél? \n'))
#     turn = int(input("Hány körös legyen? \n"))
# except ValueError:
#     print("Please enter a valid parameter!\n")


row = 5
column = 5
turn = 5

# hajok kiosztasa
ships5 = (0, 0, 2)
ships6 = (0, 0, 1, 1)
ships7 = (0, 0, 2, 1)
ships8 = (0, 0, 1, 2)
ships9 = (0, 0, 2, 1, 0, 1)

if row == 5:
    ships = ships5
elif row == 6:
    ships = ships6
elif row == 7:
    ships = ships7
elif row == 8:
    ships = ships7
elif row == 9:
    ships = ships9

# palyak
grid1 = [0] * row
i = 0
for i in range(row):
    grid1[i] = [0] * column
grid2 = copy.deepcopy(grid1)

##########################################

# hajo elhelyezes
for i in range(len(ships)):
    k = 1
    while k <= ships[i]:
        length = i
        all_good = 0
        while all_good == 0:
                # P1
            print("First player:")
            try:
                row_ship = int(input("\nRow of ship? \n")) - 1
                column_ship = int(input("\nColumn of ship? \n")) - 1
                direction = int(
                    input("\nDirection of ship? (1 is vertical, 0 is horizontal.)\n"))

            except ValueError:
                print("Please enter a valid parameter!\n")
                continue
            all_good = out_of_grid(
                grid1, row_ship, column_ship, direction, length)
            if all_good == 0:
                continue
            life1 = ship_placement(
                grid1, row_ship, column_ship, direction, length)
        k += 1
        # P2

os.system('clear')
for i in range(len(ships)):
    k = 1
    while k <= ships[i]:
        length = i
        all_good = 0
        while all_good == 0:
            print("\nSecond player:")
            try:
                row_ship = int(input("\nRow of ship? \n")) - 1
                column_ship = int(input("\nColumn of ship? \n")) - 1
                direction = int(input("\nDircetion of ship? \n"))
            except ValueError:
                print("Please enter a valid parameter!\n")
                continue
            all_good = out_of_grid(
                grid2, row_ship, column_ship, direction, length)
            if all_good == 0:
                continue
            life2 = ship_placement(
                grid2, row_ship, column_ship, direction, length)
        k += 1

# ship printeles
    # P1
# print_grid_preview(grid1)
#     #P2
# print()
# print_grid_preview(grid2)
os.system('clear')

while life1 > 0 and life2 > 0 and turn > 0:
    print_all()

# function shooting
    all_good = 0
    while all_good == 0:
        # P1
        print("\nFirst player shoots:\n")
        try:
            row_ship = int(input("Row of target?\n")) - 1
            column_ship = int(input("Column of target?\n")) - 1
        except ValueError:
            print("\nPlease enter a valid parameter!\n")
            continue
        all_good = out_of_grid(grid1, row_ship, column_ship, 1, 0)
        if all_good == 0:
            continue
        life2 = life2 - shooting(grid1, row_ship, column_ship)

        os.system('clear')
        print_all()

    all_good = 0
    while all_good == 0:
            # P2
        print("\nSecond player shoots:\n")
        try:
            row_ship = int(input("Row of target?\n")) - 1
            column_ship = int(input("Column of target?\n")) - 1
        except ValueError:
            print("\nPlease enter a valid parameter!\n")
            continue
        all_good = out_of_grid(grid2, row_ship, column_ship, 1, 0)
        if all_good == 0:
            continue
        life1 = life1 - shooting(grid2, row_ship, column_ship)

    os.system('clear')

    # print()
    # cheat_sheet(grid1)
    # print()
    # cheat_sheet(grid2)
    # print()
    turn -= 1

print_all()
if life2 == 0:
    print("\nFirst player wins!")
elif life1 == 0:
    print("\nSecond player wins!")
elif turn == 0:
    print("\nGame fucking over, mate!")
