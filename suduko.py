board = [
    [5,3,1,6,0,7,9,0,0],
    [6,0,9,8,1,0,2,5,7],
    [8,0,0,5,9,0,6,0,3],
    [4,9,0,1,0,0,8,3,2],
    [0,1,0,0,6,9,0,0,5],
    [7,0,3,2,4,0,0,0,6],
    [9,0,2,4,0,1,0,7,8],
    [0,8,5,7,0,6,0,0,9],
    [3,0,4,0,0,2,0,6,1]
]


def print_board(bo):
    for i in range(len(bo)):
        #going through every row
        if i%3==0 and i!=0:
            print(" - - - - - - - - - ")

        for j in range(len(bo[0])):
            #going through every element in the row
            if j%3==0 and j!=0:
                # printing | after every 3 element excluding start
                print("| ",end="")

            if j==8:
                # after 8th element it will print the j number and go to next line
                print(bo[i][j])
            else:
                #till it reaches the last element it will print every element with a space in between within same line
                print(str(bo[i][j]) + " ",end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                #checking for the 0 in row
                return (i,j) #row,clm

    return None


def valid(bo ,num ,pos):
    #checking row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # checking column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #Check Box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 +3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):
        if valid(bo , i , (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col] = 0

    return False




print_board(board)
solve(board)
print("----------------------")
print("----------------------")
print("----------------------")
print("----------------------")
print("----------------------")
print("----------------------")

print_board(board)


