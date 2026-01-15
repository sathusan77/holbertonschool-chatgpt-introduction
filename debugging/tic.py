#!/usr/bin/python3

def print_board(board):
    """Print the Tic Tac Toe board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if there is a winner"""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True, row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True, board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True, board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True, board[0][2]

    return False, None

def get_int_input(prompt):
    """Prompt user for a valid integer 0-2"""
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1, 2]:
                return value
            else:
                print("Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    """Main game loop"""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    max_moves = 9

    while True:
        print_board(board)
        row = get_int_input("Enter row (0, 1, or 2) for player " + player + ": ")
        col = get_int_input("Enter column (0, 1, or 2) for player " + player + ": ")

        if board[row][col] == " ":
            board[row][col] = player
            moves += 1
            winner, winner_player = check_winner(board)
            if winner:
                print_board(board)
                print("Player " + winner_player + " wins!")
                break
            if moves == max_moves:
                print_board(board)
                print("It's a tie!")
                break
            # Switch player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()

