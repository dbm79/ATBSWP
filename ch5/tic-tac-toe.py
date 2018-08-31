the_board = { 'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
              'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
              'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}

def print_board(board):

    print(f"{board['top-L']}|{board['top-M']}|{board['top-R']}")
    print('-+-+-')
    print(f"{board['mid-L']}|{board['mid-M']}|{board['mid-R']}")
    print('-+-+-')
    print(f"{board['bot-L']}|{board['bot-M']}|{board['bot-R']}")

turn = 'X'

for i in range(9):
    print_board(the_board)
    print(f"It is {turn}'s turn")
    
    print('Please enter square: ')
    move = str(input())
    
    the_board[move] = turn

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_board(the_board)