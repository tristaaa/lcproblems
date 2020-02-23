
# 小Q拿出了一块有NxM像素格的画板, 画板初始状态是空白的,用'X'表示。
# 每次小Q会选择一条斜线, 如果斜线的方向形如'/',小Q会选择这条斜线中的一段格子,都涂画为蓝色,用'B'表示;
# 如果对角线的方向形如'\',小Q会选择这条斜线中的一段格子,都涂画为黄色,用'Y'表示。
# 如果一个格子既被蓝色涂画过又被黄色涂画过,那么这个格子就会变成绿色,用'G'表示。
# 小Q已经有想画出的作品的样子, 请你帮他计算一下他最少需要多少次操作完成这幅画。

def getMinStep(n,m,board):
    """
    get the minimum steps to complete the board
    
    :type n: int, number of rows of the board, 1<=n<=50
    :type m: int, number of columns of the board, 1<=m<=50
    :type board: List[String], final version of the board, each char in string can be 'b','y','g','x'
    :rtype: int
    """
    step=0
    for i in range(n):
        for j in range(m):
            if board[i][j]=='Y':
                paintY(i,j,n,m,board)
                step+=1
            elif board[i][j]=='B':
                paintB(i,j,n,m,board)
                step+=1
            elif board[i][j]=='G':
                paintY(i,j,n,m,board)
                paintB(i,j,n,m,board)
                step+=2
    return step


def paintY(i,j,n,m,board):
    if 0<=i<n and 0<=j<m and (board[i][j]=='Y' or board[i][j]=='G'):
        if board[i][j]=='Y': board[i][j]='X'
        else: board[i][j]='B'

        paintY(i-1,j-1,n,m,board)
        paintY(i+1,j+1,n,m,board)


def paintB(i,j,n,m,board):
    if 0<=i<n and 0<=j<m and (board[i][j]=='B' or board[i][j]=='G'):
        if board[i][j]=='B': board[i][j]='X'
        else: board[i][j]='Y'

        paintB(i+1,j-1,n,m,board)
        paintB(i-1,j+1,n,m,board)

# input will be like (first row:n,m; following rows: the final version of the board):
# 4 4
# YXXB
# XYGX
# XBYY
# BXXY

# expected output: 3
n,m=map(int,input("please input the number of rows(n) and columns(m) of the board: n m=").split())
print("And given the final version of the board:")
board=[]
for i in range(n):
    board.append(list(input()))
print("\nThe minimum steps to complete the painting will be: %d" % (getMinStep(n,m,board)))
