import random

board = [" "]*10
available = [str(i) for i in range(0, 10)]
players = ["0" ,"X", "O"]
# used to choose random player from players list
def random_player_chooser():
    return random.choice((1, -1))

# Our Tic-Tac-Toe board
def display_board(a, b):
    print("\n"*100)
    print("Available Moves          Tic-Tac-Toe")
    print(" -------------           -------------")
    print(" | "+a[7]+" | "+a[8]+" | "+a[9]+" |          " + " | "+b[7]+" | "+b[8]+" | "+b[9]+" | ")
    print(" -------------           -------------")
    print(" | "+a[4]+" | "+a[5]+" | "+a[6]+" |          " + " | "+b[4]+" | "+b[5]+" | "+b[6]+" | ")
    print(" -------------           -------------")
    print(" | "+a[1]+" | "+a[2]+" | "+a[3]+" |          " + " | "+b[1]+" | "+b[2]+" | "+b[3]+" | ")
    print(" -------------           -------------")

def is_position_blank(board, position):
    return board[position] == " "

def player_input(board ,player):
    position = 0
    while position not in [i for i in range(1,10)] or not is_position_blank(board, position):
        position  = int(input("player "+ player +" Enter available position : (1-9) "))
    return position

def mark_position_on_board(a, b, position, player):
    a[position] = " "
    b[position] = player

def win_check(board , mark):
    return ((board[7] == board[8] == board[9] == mark) or   # first row
            (board[4] == board[5] == board[6] == mark) or   # second row
            (board[1] == board[2] == board[3] == mark) or   # third row
            (board[7] == board[4] == board[1] == mark) or   # first column
            (board[8] == board[5] == board[2] == mark) or   # second column
            (board[9] == board[6] == board[3] == mark) or   # third column
            (board[7] == board[5] == board[3] == mark) or   # left diagonal
            (board[9] == board[5] == board[1] == mark))     # right diagonal

def board_is_full(board):
    return " " not in board[1:]

def replay():
    return input("Do you want to play game again : Yes or No ").lower().startswith("y")

while True:
    print("Welcome To Tic-Tac-Toe")
    display_board(available, board)
    index = random_player_chooser()
    player = players[index]

    game_on = True
    while game_on:
        display_board(available, board)
        position = player_input(board ,player)
        mark_position_on_board(available, board, position, player)
        if win_check(board, player):
            display_board(available, board)
            print("Congratulations player "+ player+" you won the Game")
            game_on = False
            break
        else:
            if board_is_full(board):
                print("Game is draw")
                break
            else:
                index *= -1
                player = players[index]
    board = [" "]*10
    available = [str(i) for i in range(0,10)]

    if not replay():
        break
