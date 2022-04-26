"""
Assignment:
Tic-Tac-Toe is played according to the following rules.

The game is played on a grid that is three squares by three squares.
Player one uses x's. Player two uses o's.
Players take turns putting their marks in empty squares.
The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
If all nine squares are full and neither player has three in a row, the game ends in a draw.

"""

def create_grid():
    """
    Returns the grid to perform the game
    
    input:
        Nothing
    output:
        grid: (str) the grid
    """
    grid = f"""
1|2|3
-+-+-
4|5|6
-+-+-
7|8|9 """
    return grid

def put_answer(grid, value, position):
    """
    Given a grid puts the input value in the indicated position

    input:
        grid: (str) the grid to play
        value: (str) the value that a gamer is going to put on the grid (x or o)
        position: (str) the number of the position where the gamer wants to put the respective value
    """
    modified_grid = grid.replace(position, value)
    return modified_grid

def matrix():
    m = [[1,2,3], [4,5,6], [7,8,9]]
    fi = len(m)
    co = len(m[0])
    for i in range(fi):
        for j in range(co):
            if j == co - 1: 
                print(m[i][j], end="")
            else:
                print(m[i][j], end="|")            
        print()
        if i != fi - 1:
            print("-+-+-")
        else:
            print("")

def array():
    m = [[1,2,3], [4,5,6], [7,8,9]]
    n = 6
    # pos = m[1].index(n)
    # print(pos)

    for row_index, row in enumerate(m):
        try:
            pos = row.index(n)
            return row_index, pos
        except:
            pass    
    

def main():
    # grid = create_grid()    
    # modified_grid = put_answer(grid, "x", "2")
    # print(modified_grid)
    # m1 = modified_grid.split("\n")
    # print(m1)
    # print(len(m1))
    # print()
    matrix()
    i, j = array()
    print(f"[{i}, {j}]")



if __name__ == "__main__":
    main()