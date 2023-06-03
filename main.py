"""
Title TicTacToe
Author Suvan Banerjee
Date 29 April 2023
"""
import os #for clear screen function
import sys #for exit function
PUZZLE = [['', '', ''], ['', '', ''], ['', '', '']]#the board is handled as a list or 3x3 matrix
def tie_check():
    """it returns true if all the position are filled and works to check the tie condition it
    is the best i can to to have a stable tie checking system"""
    flag = False
    for x in range(3):
        for y in range(3):
            if PUZZLE[x][y] == "":
                flag = True
    if not flag:
        if check():
            display_board(PUZZLE)
            print("\t\tIts a Tie\n")#if you want to customize tie message edit here
            sys.exit()
def clear_screen():
    """does what it says"""
    os.system('cls' if os.name == 'nt' else 'clear')
def display_board(PUZZLE):
    """prints the current state of board when called"""
    print("\n\n")
    for x in range(3):
        print("\t", x+1, " > ", end="\t")#Prints Coordinate of cells for asthetics
        for y in range(3):
            if PUZZLE[x][y]:
                print(PUZZLE[x][y], end=' | ')
            else:
                print(" ", end=' | ')
        print()
    print("\t\t ^   ^   ^")#Prints Coordinate of cells for asthetics
    print("\t\t 1   2   3\n")#Prints Coordinate of cells for asthetics
def put(POSITION, current_player):
    """it places a marker on board and returns 1 and if move is invalid it returns 0"""
    x, y = POSITION[0], POSITION[1]
    if PUZZLE[x][y] == '':
        PUZZLE[x][y] = current_player
        return 1
    else:
        return 0
def check():
    """Bruteforce check for all winning combinations if any one of the player wins
    return 0 else returns 1"""
    if (PUZZLE[0][0] == 'O'and PUZZLE[0][1] == 'O'and PUZZLE[0][2] == 'O'or
            PUZZLE[1][0] == 'O'and PUZZLE[1][1] == 'O'and PUZZLE[1][2] == 'O'or
            PUZZLE[2][0] == 'O'and PUZZLE[2][1] == 'O'and PUZZLE[2][2] == 'O'or
            PUZZLE[0][0] == 'O'and PUZZLE[1][0] == 'O'and PUZZLE[2][0] == 'O'or
            PUZZLE[0][1] == 'O'and PUZZLE[1][1] == 'O'and PUZZLE[2][1] == 'O'or
            PUZZLE[0][2] == 'O'and PUZZLE[1][2] == 'O'and PUZZLE[2][2] == 'O'or
            PUZZLE[0][0] == 'O'and PUZZLE[1][1] == 'O'and PUZZLE[2][2] == 'O'or
            PUZZLE[0][2] == 'O'and PUZZLE[1][1] == 'O'and PUZZLE[2][0] == 'O'):
        return 0
    elif (PUZZLE[0][0] == 'X'and PUZZLE[0][1] == 'X'and PUZZLE[0][2] == 'X'or
          PUZZLE[1][0] == 'X'and PUZZLE[1][1] == 'X'and PUZZLE[1][2] == 'X'or
          PUZZLE[2][0] == 'X'and PUZZLE[2][1] == 'X'and PUZZLE[2][2] == 'X'or
          PUZZLE[0][0] == 'X'and PUZZLE[1][0] == 'X'and PUZZLE[2][0] == 'X'or
          PUZZLE[0][1] == 'X'and PUZZLE[1][1] == 'X'and PUZZLE[2][1] == 'X'or
          PUZZLE[0][2] == 'X'and PUZZLE[1][2] == 'X'and PUZZLE[2][2] == 'X'or
          PUZZLE[0][0] == 'X'and PUZZLE[1][1] == 'X'and PUZZLE[2][2] == 'X'or
          PUZZLE[2][0] == 'X'and PUZZLE[1][1] == 'X'and PUZZLE[0][2] == 'X'):
        return 0
    else:
        return 1
def main():
    """Main function"""
    while True:
        player = ['X', 'O']#If you want to change players change it here.
        print("\n\tFirst Player want to play as ", player[0], " or ", player[1], "\n")
        current_player = input("\t").upper()
        if current_player in player:
            clear_screen()
            break
        else:
            clear_screen()
            print("\t Enter a valid Character")
    while check():
        try:
            display_board(PUZZLE)
            print("\n\tEnter the desired position to put a ", current_player, "\n")
            POSITION = list(map(int, input("\t").split()))
            POSITION[0], POSITION[1] = POSITION[0]-1, POSITION[1]-1
            clear_screen()
            if len(POSITION) > 2 and POSITION[0] > 2 and POSITION[1] > 2:
                print("\tInvalid move")
            else:
                if not put(POSITION, current_player):
                    raise SyntaxError#any other error can also be raised.
            current_player = player[0] if current_player == player[1] else player[1]
            tie_check()
        except IndexError:
        #This block handles the condition when player tries to move on a index greater than 3
            clear_screen()
            print("\tChoose a move that is inside the range (1 to 3 inclusive)")
        except ValueError:
        #This block handles the condition when input is not in proper format
            clear_screen()
            print("\tOnly two space-seperated numbers are allowed (example 1 1 or 1 2 etc)")
        except SyntaxError:
        #This block handles the condition when player tries to move on a already marked cell
            clear_screen()
            print("\t\tCannot Move here")
    current_player = player[0] if current_player == player[1] else player[1]
    display_board(PUZZLE)
    print("\n\tPlayer ", current_player, "Wins\n\n")
    #If you want to change win prompt ^ change it here.
if __name__ == "__main__":
    clear_screen()#just for asthetics
    main()#main function call
