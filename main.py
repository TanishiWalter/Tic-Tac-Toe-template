#This file is gonna manage all the other parts, and merge them together.

import functions

winVar = False
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
turn = "X"

functions.printGrid(grid)

while winVar == False:
  winVar = functions.updateGrid(grid)
  if winVar == True:
    break
  try:
    functions.playerTurn(grid, turn)
  except Exception as e:
    print(e)
    continue
  functions.printGrid(grid)
  functions.updateGrid(grid)
  functions.playerChecker(turn, winVar)
  if winVar == True:
    break
  turn = functions.playerChanger(turn)
  winVar = functions.winChecker(grid, turn, winVar)
  if winVar == True:
    break
