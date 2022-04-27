"""
Assignment:
Tic-Tac-Toe is played according to the following rules.

The game is played on a grid that is three squares by three squares.
Player one uses x's. Player two uses o's.
Players take turns putting their marks in empty squares.
The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
If all nine squares are full and neither player has three in a row, the game ends in a draw.


Ramón Felipe Castaño Salgado
"""


def show_matrix(matrix):
    """
    Given a list of list (matrix) return a formated string with the matrix values:
    1|2|3
    -+-+-
    4|5|6
    -+-+-
    7|8|9

    input:
        matrix: (list of list [int]) list of list with the int numbers
    """

    # matrix = [[1,2,3], [4,5,6], [7,8,9]]
    fi = len(matrix)
    co = len(matrix[0])
    for i in range(fi):
        for j in range(co):
            if j == co - 1: 
                print(matrix[i][j], end="")
            else:
                print(matrix[i][j], end="|")            
        print()
        if i != fi - 1:
            print("".join(["-+-"] * (fi -1)))
        else:
            print("")



def find_position(matrix, n):
    """
    Given a list of list and a number return the position of the number in the list of list

    input:
        matrix: (list of list) list of list to process
        n: (int) number to find

    output: 
        found_row, found_col: (tuple) the coordinates of n
    """
    found_row = None
    found_col = None

    for row_index, row in enumerate(matrix):        
        try:
            pos = row.index(n)            
            found_row = row_index
            found_col = pos
            break
        except:
            continue
    return found_row, found_col  




def put_value(matrix, i, j, value):
    """
    Put in a list of list the given value in the indicated position

    input: 
        matrix: (list of list) list of list to process
        i: (int) index of the row
        j: (int) index of the column
        value: (str) value to put in the list of list
    
    output:
        N/A
    """
    matrix[i][j] = value
   

def ask_input(player):
    """"
    Ask an input value by console
    input:
        player: (str) the player nickname

    output: 
        (str) the input from user
    """
    return int(input(f"{player}'s turn to choose a square (1-9): "))


def comparision(to_compare): 
    """
    Compares an input string to determine if three consecutives values are equal

    input:
        to_compare: (str) value to be examined
    output:
        (bool) True if the input is in the possible answers, False otherwise
    """   
    return to_compare == "xxx" or to_compare == "ooo"
        

def is_winner(matrix):
    """
    Given a list of list determin if there is a winner. It looks by column, row, main diagonal and secondary diagonal

    input:
        matrix: (list of lists) 
    output:
        won: (bool) True if there is a winner. False in otherwise
    """
    won = False
    for j in range(len(matrix)):
        by_column = "".join(list(map(str, [val[j] for val in matrix]))) 
        by_row = "".join(list(map(str, matrix[j])))
        by_main_diag = "".join(list(map(str, [diag[index] for index, diag in enumerate(matrix)])))
        by_sec_diag = "".join(list(map(str, [diag[len(matrix) -1 - index] for index, diag in enumerate(matrix)])))
        if comparision(by_column) or comparision(by_row) or comparision(by_main_diag) or comparision(by_sec_diag):
            won = True
            break
        else:
            continue    
    return won



def all_type_str(matrix):
    """
    Figures out if all the elements of a list of lists are type string

    input: 
        matrix: (list of lists)
    output:
        (bool) True if all elements are type string. False otherwise.
    """
    counter = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if type(matrix[i][j]) == str:
                counter += 1
    return counter == rows * cols
    


def main():
    m = [[1,2,3], [4,5,6], [7,8,9]]
    show_matrix(m)

    won = False
    count = 1
    
    while won == False:
        if count % 2 == 0:
            player = "o"
        else:
            player = "x"
        selected = ask_input(player)
        
        i, j = find_position(m, selected)
        if i != None and j != None:
            put_value(m, i, j, player)            
            won = is_winner(m)            
        show_matrix(m)
        
        if all_type_str(m):
                break

        count += 1
    print("Good game. Thanks for playing!")


if __name__ == "__main__":
    main()
    