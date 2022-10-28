#This is file with all the basic functions

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

def playerChecker(turnP, onOffP):
  if turnP != "X" and "O":
    print("Error, the turn wariable is not X or O. \n This may be because of not-working modification, please, check the code!")
    winVarW = True

#Misc part:

def winChecker(gridW, turnW, winVarW):
  winWar = [gridW[0][0], gridW[0][1], gridW[0][2]] == ["O","O", "O"] or ["X","X","X"]
  winWar2 = [gridW[1][0], gridW[1][1], gridW[1][2]] == ["O","O", "O"] or ["X","X","X"]
  winWar3 = [gridW[2][0], gridW[2][1], gridW[2][2]] == ["O","O", "O"] or ["X","X","X"]
  winWar4 = [gridW[0][0], gridW[1][0], gridW[2][0]] == ["O","O", "O"] or ["X","X","X"]
  winWar5 = [gridW[0][1], gridW[1][1], gridW[2][1]] == ["O","O", "O"] or ["X","X","X"]
  winWar6 = [gridW[0][2], gridW[1][2], gridW[2][2]] == ["O","O", "O"] or ["X","X","X"]
  winWar7 = [gridW[0][0], gridW[1][1], gridW[2][2]] == ["O","O", "O"] or ["X","X","X"]
  winWar8 = [gridW[2][2], gridW[1][1], gridW[2][0]] == ["O","O", "O"] or ["X","X","X"]
  if winWar or winWar2 or winWar3 or winWar4 or winWar5 or winWar6 or winWar7 or winWar8 == True:
    print("Player" + turnW + "won!")
    winVarW = True
  else:
    for gridW in i:
      if i != "O" or "X" or 0:
        print("Tie!")
        winVarW = True