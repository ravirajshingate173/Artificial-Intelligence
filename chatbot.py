def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there is a winner."""
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 will be X and Player 2 will be O.")
    print("Each player will take turns entering their move.")

    # Initialize the empty board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)

    current_player = 'X'
    while True:
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
        except ValueError:
            print("Please enter valid row and column numbers.")
            continue

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
            board[row][col] = current_player
            print_board(board)

            if check_winner(board):
                print(f"Player {current_player} wins!")
                break

            if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                print("It's a draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Please try again.")

if __name__ == "__main__":
    tic_tac_toe()
