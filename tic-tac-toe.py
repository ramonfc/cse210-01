"""
Assignment:
Tic-Tac-Toe is played according to the following rules.

The game is played on a grid that is three squares by three squares.
Player one uses x's. Player two uses o's.
Players take turns putting their marks in empty squares.
The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
If all nine squares are full and neither player has three in a row, the game ends in a draw.

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
    matrix[i][j] = value
   

def ask_input(player):
    return int(input(f"{player}'s turn to choose a square (1-9): "))


def comparision(to_compare):    
    if to_compare == "xxx" or to_compare == "ooo":
        return True           


def is_winner(matrix):
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
    