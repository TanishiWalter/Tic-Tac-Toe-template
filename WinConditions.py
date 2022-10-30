#This is list of variables, that detects, if player X or O wined

def variables(gridW):
  winWaO = bool([gridW[0][0], gridW[0][1], gridW[0][2]] == ["O","O", "O"])
  winWarO2 = bool([gridW[1][0], gridW[1][1], gridW[1][2]] == ["O","O", "O"])
  winWarO3 = bool([gridW[2][0], gridW[2][1], gridW[2][2]] == ["O","O", "O"])
  winWarO4 = bool([gridW[0][0], gridW[1][0], gridW[2][0]] == ["O","O", "O"])
  winWarO5 = bool([gridW[0][1], gridW[1][1], gridW[2][1]] == ["O","O", "O"])
  winWarO6 = bool([gridW[0][2], gridW[1][2], gridW[2][2]] == ["O","O", "O"])
  winWarO7 = bool([gridW[0][0], gridW[1][1], gridW[2][2]] == ["O","O", "O"])
  winWarO8 = bool([gridW[2][2], gridW[1][1], gridW[2][0]] == ["O","O", "O"])
  winWarX = bool([gridW[0][0], gridW[0][1], gridW[0][2]] == ["X","X", "X"])
  winWarX2 = bool([gridW[1][0], gridW[1][1], gridW[1][2]] == ["X","X", "X"])
  winWarX3 = bool([gridW[2][0], gridW[2][1], gridW[2][2]] == ["X","X", "X"])
  winWarX4 = bool([gridW[0][0], gridW[1][0], gridW[2][0]] == ["X","X", "X"])
  winWarX5 = bool([gridW[0][1], gridW[1][1], gridW[2][1]] == ["X","X", "X"])
  winWarX6 = bool([gridW[0][2], gridW[1][2], gridW[2][2]] == ["X","X", "X"])
  winWarX7 = bool([gridW[0][0], gridW[1][1], gridW[2][2]] == ["X","X", "X"])
  winWarX8 = bool([gridW[2][2], gridW[1][1], gridW[2][0]] == ["X","X", "X"])

  winVarList = [winWaO,winWarO2,winWarO3,winWarO4,winWarO5,winWarO6,winWarO7,winWarO8,winWarX,winWarX2,winWarX3,winWarX4,winWarX5,winWarX6,winWarX7,winWarX8]  

  return(winVarList)
  
  