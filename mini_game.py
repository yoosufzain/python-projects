board = ["*" for i in range(9)]
def create_board():
    print(" ",board[0],"|",board[1],"|",board[2])
    print("------------")
    print(" ",board[3],"|",board[4],"|",board[5])
    print("------------")
    print(" ",board[6],"|",board[7],"|",board[8])
def check_win(player):
   win_change =  [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
   for check in win_change:
       if board[check[0]] == player and board[check[1]] == player and board[check[2]] == player :
           return 1
   else:
       return 0
     
        
def game():
    create_board()
    player1 ="X"
    player2 ="O"
    while True:
        while True:
            player1_position = input(f"{player1} Enter your position")

            if player1_position not in [str(i) for i in range(1,10)] :
                print("This position is out of range")
            else:
                if board[int(player1_position)-1] =="*" :
                    board[int(player1_position)-1] =player1
                    create_board()
                    if len( [i for i in board if i == "*"] )== 0:
                        return "Match is draw"
                        
                    if check_win(player1):
                        return "X is win"
                    break
                else:
                    print("This place is not empty")

        
        while True:
            player2_position = input(f"{player2} Enter your position")

            if  player2_position not in [str(i) for i in range(1,10)] :
                print("This position is out of range")
            else:
                if board[int(player2_position)-1] =="*" :
                    board[int(player2_position)-1] =player2
                    create_board()
                    if len( [i for i in board if i == "*"] )== 0:
                        return "Match is draw1"
                        
                    if check_win(player2):
                        return "O is win"
                    break

                else:
                    print("This place is not empty")
        
print(game())
while True:
    board = ["*" for i in range(9)]
    suggestion = input("Do yo want to play [Y/N]")
    if suggestion in "Yy":
        print(game())
    else :
        exit()