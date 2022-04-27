
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

def win_by_col(matrix):
    won = False
    for j in range(len(matrix)):
        to_compare = "".join(list(map(str, [val[j] for val in matrix]))) 
        if to_compare == "xxx" or to_compare == "ooo":
            won = True
            break
        else:
            continue
    return won


def comparision(to_compare):    
    if to_compare == "xxx" or to_compare == "ooo":
        return True           


def is_winner(matrix):
    won = False
    for j in range(len(matrix)):
        by_column = "".join(list(map(str, [val[j] for val in matrix]))) 
        by_row = "".join(list(map(str, matrix[j])))
        by_main_diag = "".join(list(map(str, [m[index][index] for index in range(len(m))])))
        by_sec_diag = "".join(list(map(str, [matrix[index][len(matrix) -1 - index] for index in range(len(matrix))])))
        if comparision(by_column) or comparision(by_row) or comparision(by_main_diag) or comparision(by_sec_diag):
            won = True
            break
        else:
            continue    
    return won

m = [
["o", "o", "x"], 
["x", "o", "o"], 
["o", "x", "o"]
]
# m = [[1,2,3], [4,5,6], [7,8,9]]
m = [[1,"x",3], [4,"o",6], [7,"o",9]]
m = [[1,2,"x"], [4,"x",6], ["x",8,1]]
won = is_winner(m)
print(won)
