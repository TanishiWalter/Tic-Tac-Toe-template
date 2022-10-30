#This is file with all the basic functions

import WinConditions

#Grid part:

def printGrid(gridPrint):
  for i in gridPrint:
    print(i)

def updateGrid(gridUpdate):
  for i in gridUpdate:
    for a in i:
      if i == "X" or "O" or 0:
        continue
      else:
        print("Error in grid, invalid character!")
        return(True)
        break

#Player part:

def playerTurn(gridP, turnP):
  inputVar = input(turnP + ":")
  inputVarSpl = inputVar.split(" ")
  for i in inputVarSpl:
    try:
      Test = int(i)
    except Exception as e:
      continue
  gridP[int(inputVarSpl[0])][int(inputVarSpl[1])] = turnP

def playerChanger(turnP):
  if turnP == "X":
    return("O")
  elif turnP == "O":
    return("X")
  else:
    return("Null")

def playerChecker(turnP, winVarW):
  if turnP == "X" or "O":
    Dummy = 3
  else:
    print("Error, the turn wariable is not X or O. \n This may be because of not-working modification, please, check the code!")
    return True

#Misc part:

def winChecker(gridW, turnW, winVarW):
  for i in WinConditions.variables(gridW):
    if i == True:
      turnW = playerChanger(turnW)
      print("Player " + turnW + " won!")
      return True
    else:
      for i in gridW:
        for a in i:
          if a == "x" or "O" or 0:
            continue
          else:
            print(str(a))
            print("Tie!")
            return True
  return False
            