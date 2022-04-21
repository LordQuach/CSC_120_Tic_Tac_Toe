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
  if player_id == 1:
    check = "X"
  else:
    check = "O"
  
  #rows
  for i in range(3):
    win = True
    for j in range(3):
      if board[i][j] != check:
        win = False
        break
    if win:
      return win

  #columns
  for i in range(3):
    win = True
    for j in range(3):
      if board[j][i] != check:
        win = False
        break
    if win:
      return win
  
  #diagonals
  win = True
  for i in range(3):
    if board[i][i] != check:
      win = False
      break
  if win:
      return win
  
  win = True
  for i in range(3):
    if board[i][2 - i] != check:
      win = False
      break
  if win:
    return win
  return False

def check_tie():
  for row in board:
    for item in row:
      if item == '-':
        return False
  return True

def switch_player(player_id):
  if player_id == 2:
    print("Player 1's turn.")
    return 1
  else:
    print("Player 2's turn.")
    return 2

def main():
  player_id = 1
  print("Player 1's turn.")
  print_board()
  while True:
    #Get input from player 1 to place a mark
    row, col = map(int, input("Please choose a spot to place your mark. ").split(","))

    #Check input loop
    if check_mark(row,col) == True:
      place_mark(row,col,player_id)
    else:
      print("You can't place a mark here.")
      row, col = map(int, input("Please choose a spot to place your mark. ").split(","))

    #Check for game end
    if check_win(player_id) == True:
      print("Player " + str(player_id) + " has won!")
      print_board()
      break
    if check_tie() == True:
      print("It's a tie!")
      print_board()
      break
    
    #Next player's turn
    player_id = switch_player(player_id)

    #Show the board
    print_board()

#Start the game
main()