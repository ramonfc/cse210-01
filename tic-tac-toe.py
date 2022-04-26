"""
Assignment:
Tic-Tac-Toe is played according to the following rules.

The game is played on a grid that is three squares by three squares.
Player one uses x's. Player two uses o's.
Players take turns putting their marks in empty squares.
The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
If all nine squares are full and neither player has three in a row, the game ends in a draw.

"""



from numpy import matrix


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


def win_by_row(matrix):
    won = False
    for row in matrix:
        to_compare = "".join(map(str, row))
        if to_compare == "xxx" or to_compare == "ooo":
            won = True
            break
        else:
            continue
    return won
        


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
            won = win_by_row(m)
        show_matrix(m)
    
        count += 1



if __name__ == "__main__":
    main()