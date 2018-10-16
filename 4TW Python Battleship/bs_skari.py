Rows = 0
Columns = 0

print("Welcome to battleship!")

while (Rows <= 0) or (Columns <= 0) :
   Rows = int(input("Please enter the number of rows you want: \n"))
   Columns = int(input("Please enter the number of columns you want: \n"))

def create_grid(Rows, Columns):
    grid = []
    for row in range(Rows):
        row = []
        for col in range(Columns):
           row.append(' ')
        grid.append(row)
    return grid

def display_grid(grid, Columns):
    column_names = ('abcdefghijklmnopqrstuvwxyz'[:Columns])
    print('  | ' + ' | '.join(column_names.upper()) + ' |')
    for number, row in enumerate(grid):
        print(number + 1, '| ' + ' | '.join(row) + ' |')

grid = create_grid(Rows, Columns)
display_grid(grid, Columns)