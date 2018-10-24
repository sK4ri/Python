import random

Rows = 0
Columns = 0
turns = 0

print("Welcome to battleship!")

while (Rows > 10) or (Columns > 10) or (Rows <= 0) or (Columns <= 0):
   Rows = int(input("Please enter the number of rows you want. \n"))
   Columns = int(input("Please enter the number of columns you want. \n"))

def create_grid(Rows, Columns):
   grid = []
   for row in range(Rows):
       row = []
       for col in range(Columns):
           row.append(' ')
       grid.append(row)
   return grid

def display_grid(grid, Columns):
   column_names = 'abcdefghijklmnopqrstuvwxyz'[:Columns]
   print('  | ' + ' | '.join(column_names.upper()) + ' |')
   for number, row in enumerate(grid):
      print(number + 1, '| ' + ' | '.join(row) + ' |')

grid = create_grid(Rows, Columns)
display_grid(grid, Columns)

# def random_row(grid):
#    return random.randint(1,len(grid))

# def random_col(grid):
#    return random.randint(1,len(grid[0]))

def update_gridHit(grid, GuessRow, GuessColumn):
   grid[GuessRow-1][GuessColumn-1] = 'O'

def update_gridMiss(grid, GuessRow, GuessColumn):
   grid[GuessRow-1][GuessColumn-1] = 'X'

ShipRow = random_row(grid)
ShipColumn = random_col(grid)

while (turns != 5):
   GuessRow = int(input("What row do you guess? \n"))
   GuessColumn = int(input("What column do you guess? \n"))

   if (GuessRow == ShipRow) and (GuessColumn == ShipColumn):
       turns += 1
       update_gridHit(grid, GuessRow, GuessColumn)
       display_grid(grid, Columns)
       print("You hit the battleship! Congratulations!")
       break

   else:
       if (GuessRow < 1 or GuessRow > Rows) or (GuessColumn < 1 or GuessColumn > Columns):
           print("Outside the set grid. Please pick a number within it your Rows and Columns.")

       elif (grid[GuessRow-1][GuessColumn-1] == "X"):
           print("You guessed that already.")

       else:

           turns += 1
           print("You missed the ship.")
           update_gridMiss(grid, GuessRow, GuessColumn)
           display_grid(grid, Columns)

   if (turns >= 5):
       print("Game over! You ran out of tries")