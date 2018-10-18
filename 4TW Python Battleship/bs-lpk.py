row = int(input('How many rows do you want? \n'))
column = int(input('How many column do you want? \n'))
boat1 = int(input('What is the row of the boat? \n'))
boat2 = int(input('What is the column of the boat? \n'))
boat3 = int(input('Placement of ship horisontal (0) or vertical (1)? \n'))
boat4 = int(input('Lenght of the ship? \n'))

grid = [0] * row
grid_boat = [0] * row

life = boat4
turn = 5

#hajo placement ??????????????????
i = 0
for i in range(row):
    grid_boat[i] = [0] * column

#hajo fuggoleges es vizszintes elhelyezese
z = 0
i = 0
k = 0
if boat3 == 1:
    for x in range(len(grid_boat)):
        for y in range(len(grid_boat[i])):
            if boat1 == z and boat2 == i:
                grid_boat[z][i] = "X"
                i += 1
                k += 1
            elif boat1 < z and boat2 == i:
                while k < boat4:
                    grid_boat[z][i] = "X"
                    k += 1
                    i += 1
                    break
            else:
                grid_boat[z][i] = 0
                i += 1
        i = 0
        z += 1
elif boat3 ==0:
    for x in range(len(grid_boat)):  
        i = 0
        if boat1 == z:
            for y in range(len(grid_boat[i])):
                
                if boat2 == i and boat3 == 0:
                    while k < boat4:
                        grid_boat[z][i] = "X"
                        k += 1
                        i += 1
                i += 1
            z += 1
        else:
            for y in range(len(grid_boat[i])):
                i += 1
            z += 1
        print()
#hajo elhelyezes idaig

print(grid_boat)

#boat printeles
z = 0
for x in range(len(grid_boat)):
    i = 0
    for y in range(len(grid_boat[i])):
        print(grid_boat[z][i], end = " ")
        i += 1
    z += 1
    print()


while life > 0 or turn > 0:
    print("Turns left:", turn)
    shot1 = int(input('Row of shooting? \n'))
    shot2 = int(input('Column of shooting? \n'))

    #fogofwar pálya
    # for i in range(row):
    #     grid[i] = [0] * column
    # z = 0
    # for x in range(len(grid)):
    #     i = 0
    #     for y in range(len(grid[i])):
    #         print(grid[z][i], end = " ")
    #         i += 1
    #     z += 1
    #     print()
    # print(grid)

    #shooting
    z = 0
    i = 0 
    for x in range(len(grid_boat)):   
        if shot1 == z:
            for y in range(len(grid_boat[i])):
                if shot2 == i:
                    if grid_boat[z][i] == 0:
                        grid_boat[z][i] = "#"
                        i += 1
                    else:
                        grid_boat[z][i] = "H"
                        i += 1 
                        life -= 1
                i += 1
        z += 1

    print(grid_boat)

    #boat printeles
    z = 0
    for x in range(len(grid_boat)):
        i = 0
        for y in range(len(grid_boat[i])):
            print(grid_boat[z][i], end = " ")
            i += 1
        z += 1
        print()

    #fogofwar akco utan
    print()
    z = 0
    for x in range(len(grid_boat)):
        i = 0
        for y in range(len(grid_boat[i])):
            if grid_boat[z][i] == "#" or grid_boat[z][i] == "H":
                print(grid_boat[z][i], end = " ")
                i += 1
            else:
                print(0, end = " ")
                i += 1
        z += 1
        print()
    turn -= 1