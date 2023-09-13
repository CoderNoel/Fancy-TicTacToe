""" A fancy tic-tac-toe game for CSSE1001/7030 A1. """
from constants import *

# Developed by Noel
# University of Queensland, Student ID: 48422819
# Email: n.karayampully@uqconnect.edu.au

Board = list[list[str]]
Pieces = list[int]
Move = tuple[int, int, int]

# Write your functions here

# 4.1
def num_hours() -> float:
    # Returns total estimated time worked on the project in float type.
    hours = 8.0
    return hours

# 4.2
def generate_initial_pieces(num_pieces: int) -> Pieces:
    '''
    This function takes in an integer and returns a list starting from 1 uptill including the entered integer. 
    >>> generate_initial_pieces(5)
    [1, 2, 3, 4, 5]
    '''
    initial_pieces = []
    for i in range(1, num_pieces + 1):
        initial_pieces.append(i)
    return initial_pieces

# 4.3
def initial_state() -> Board: 
    '''
    Returns an empty board in the form of list within a list where every cell is empty. 
    >>> initial_state()
    [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    '''
    board = [[EMPTY] * 3 for i in range(3)]
    return board

# 4.4
def place_piece(board: Board, player: str, pieces_available: Pieces, move: Move ) -> None:
    '''
    Update the board by placing the player's piece and updating available pieces.
    
    Parameters:
    - board (List[List[str]]): Current game board.
    - available_pieces (List[int]): Remaining pieces for the player.
    - player (str): Current player ('O' or 'X').
    - move (Tuple[int, int, int]): Desired placement as (row, column, size).

    Returns:
    None

    >>> place_piece(board, NAUGHT, pieces, (1, 1, 3)) 
    >>> board
    [[' ',' ',' '],[' ','O3',' '],[' ',' ',' ']]
    '''
    player_move = player
    player_move += str(move[2]) 
    board[move[0]] [move[1]] = player_move # Assigns the player_move to the appropriate index of the board.
    pieces_available.remove(move[2])
    return board

# 4.5
def print_game(board: Board, naught_pieces: Pieces, cross_pieces: Pieces) -> None:
    '''
    Display the current game state in a user-friendly format.
    
    Parameters:
    - board (Board): The current game board.
    - naught_pieces (Pieces): Remaining pieces for the 'O' player.
    - cross_pieces (Pieces): Remaining pieces for the 'X' player.

    Returns:
    None
    '''
    def output_message(symbol, pieces) -> str: 
        message = f"{symbol} has: "
        for i in pieces:
            if i != pieces[-1]: # To avoid commas and spaces after the last piece.
                message += (str(i) + ", ")
            else:
                message += str(i)
        return message
    
    print(output_message(NAUGHT, naught_pieces))
    print(output_message(CROSS, cross_pieces))

    print("\n   1  2  3")
    for i in range(3):
        print("  " + "-" * 9)
        print(f"{i+1}|{board[i][0]}|{board[i][1]}|{board[i][2]}|")
    print("  " + "-" * 9)

# 4.6
def process_move(move: str) -> Move | None:
    '''
    Converts a move string to a tuple representing the move details.

    Parameters:
    - move (str): A string describing the move, formatted as 'row column piece size'.

    Returns:
    - Move: A tuple of three integers (row, column, piece size) if the conversion is successful.
    - None: If the move is in an invalid format.
    
    >>> process_move('3 3 5')
    (2, 2, 5)
    '''
    rows_or_columns = ["1", "2", "3"]
    sizes = [str(i) for i in range(1, PIECES_PER_PLAYER + 1)]

    # Checks if the move is 5 characters long and contain 3 non-space characters each separated by space.
    if len(move)!= 5 or move[::2] == " " or move.count(" ") != 2:
        print(INVALID_FORMAT_MESSAGE)
    
    # Checks for invalid row
    elif move[0] not in rows_or_columns:
        print(INVALID_ROW_MESSAGE)

    # Checks for invalid column
    elif move[2] not in rows_or_columns:
        print(INVALID_COLUMN_MESSAGE)

    # Checks for invalid size
    elif move[4] not in sizes:
        print(INVALID_SIZE_MESSAGE)

    # Converts the move string into a tuple of integers
    else:
        board_moves = move.split()
        moves = []
        for i in range(len(board_moves)-1):
            moves.append(int(board_moves[i])-1)
        moves.append(int(board_moves[-1]))
        move_details = tuple(moves)
        return move_details

# 4.7    
def get_player_move() -> Move: 
    '''
    Prompt the user for a move continuously until a valid move is entered.

    Returns:
    - Move: A tuple of integers representing the move in the format (row, column, size).

    Notes:
    - Displays a help message if the user enters 'h' or 'H'.
    - If the move entered is in an invalid format, relevant error messages will be displayed.

    >>> get_player_move()
    Enter your move: 1 1 1
    (0, 0, 1)
    '''
    while True:
        player_input = input("Enter your move: ")

        if player_input.lower() == "h":
            print(HELP_MESSAGE)
        
        else:
            player_move = process_move(player_input)
            if player_move != None:
                return player_move

# 4.8
def check_move(board: Board, pieces_available: Pieces, move: Move) -> bool:
    '''
    Check if a move is valid based on the current board and available pieces.
    
    Parameters:
    - board (Board): Current game state.
    - pieces_available (Pieces): Pieces the player has left.
    - move (Move): Intended move as (row, column, piece size).
    
    Returns:
    - bool: True if valid, False otherwise.
    '''
    position = board [move[0]] [move[1]]
    if move[-1] in pieces_available:
        if position == EMPTY or int(position[1]) < move[2]:
            return True
    return False

# 4.9
def check_win(board: Board) -> str | None: 
    '''
    Determine the winner of the game, if any.
    
    Parameters:
    - board (Board): Current game state.
    
    Returns:
    - str: Player symbol 'O' or 'X' if there's a winner.
    - None: If no winner is found.

    >>> board = [['O1', 'O2', 'O3'], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    >>> check_win(board)
    'O'
    '''
    # Check for winning rows
    for row in board:
        if row[0][0] == row[1][0] == row[2][0] and row[0] != EMPTY:
            return row[0][0]
    
    # Check for winning columns
    for column in range(3):
        if board[0][column][0] == board[1][column][0] == board[2][column][0] and board[0][column] != EMPTY:
            return board[0][column][0]

    # Check for both diagonal wins
    if board[0][0][0] == board[1][1][0] == board[2][2][0] and board[0][0] != EMPTY:
        return board[0][0][0]
        
    if board[0][2][0] == board[1][1][0] == board[2][0][0] and board[0][2] != EMPTY:
        return board[0][2][0]

# 4.10    
def check_stalemate(board: Board, naught_pieces: Pieces, cross_pieces: Pieces) -> bool:
    '''
    Determines if the game is in a stalemate state.
    
    Parameters:
    - board (Board): The current state of the game board.
    - naught_pieces (Pieces): Pieces available for the 'O' player.
    - cross_pieces (Pieces): Pieces available for the 'X' player.
    
    Returns:
    - bool: True if game is in stalemate, else False.
    '''
    # Combine the available pieces of both players
    total_available_pieces = naught_pieces + cross_pieces

    for rows in board:
        for board_piece in rows:
            if board_piece == EMPTY: # If any cell is empty, game is not stalemate. 
                return False
            
            # Check if any larger piece can be placed on top of an existing one
            for piece in total_available_pieces:
                if piece > int(board_piece[1]):
                    return False
    # If no cells are left for a move, returns True indicating a stalemate.
    return True
            
# 4.11
def main() -> None:
    while True: # Outer loop to handle game replays
        Board = initial_state()
        Pieces = generate_initial_pieces(PIECES_PER_PLAYER)
        Naught_Pieces, Cross_Pieces = Pieces.copy(), Pieces.copy()
        Player = NAUGHT # initial player

        def invalid_move(moves) -> bool:
            Board_Position = Board[moves[0]][moves[1]]
            if Board_Position != EMPTY:
                if Board_Position == f"{Player}{moves[2]}" or moves[2] <= int(Board_Position[1]):
                    print(INVALID_MOVE_MESSAGE)
                    return True
            return False 

        # Print the initial empty board state
        print_game(Board, Naught_Pieces, Cross_Pieces)

        while True: # Inner loop for the gameplay
            
            valid = False
            while not valid:
                print(f"\n{Player} turn to move\n")
                Move = get_player_move()
                if Move != None:
                    valid = not invalid_move(Move)
                              
            # Placing Player Pieces
            if Player == NAUGHT:
                Board = place_piece(Board, Player, Naught_Pieces, Move)
            else:
                Board = place_piece(Board, Player, Cross_Pieces, Move)

            # Print the game board after the move has been made
            print_game(Board, Naught_Pieces, Cross_Pieces)

            if check_win(Board) == Player:
                print(f"{Player} wins!") 
                break
            
            if check_stalemate(Board, Naught_Pieces, Cross_Pieces):
                print("Stalemate!")
                break          

            # Switching player turns
            if Player == NAUGHT:
                Player = CROSS
            else:
                Player = NAUGHT
        
        rematch = input("Play again? ")
        if rematch.lower() != 'y':
            break
        

if __name__ == '__main__':
    main()