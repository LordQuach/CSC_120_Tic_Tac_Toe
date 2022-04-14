board = []
for i in range(3):
  row = []
  for j in range(3):
    row.append("-")
  board.append(row)

def print_board():
  for row in board:
    print(row)
  print()

print_board()

def check_mark(row,col):
  if board[row][col] == "-":
    return True
  else:
    return False

def place_mark(row,col,player_id):
  if player_id == 1:
    board[row][col] = "X"
  elif player_id == 2:
    board[row][col] = "O"
  else:
    print("Invalid Player")

def check_win(player_id):
  win = True
  if player_id == 1:
    for i in range(3):
      for j in range(3):
        if board[i][j] != "X" and board[j][i] != "X":
          win = False
    for i in range(3):
      if board[i][i] != "X":
        win = False
    for i in range(3):
      if board[i][2 - i] != "X":
        win = False

def main():
  print("Testing print_board")
  print_board()

  print("Checking if 1,1 is -")
  print(check_mark(1,1))

  print("If check_mark is true, then place the mark.")
  if check_mark(1,1) == True:
    place_mark(1,1,1)
  print_board()

  print("Check if player has won.")
  if check_win(1) == True:
    print("Player 1 has won!")
  else:
    print("")

main()