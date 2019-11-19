class Solution:
    def solve(self, board):
        """
        Flipping all 'O's into 'X's in that surrounded region, 
        surrounded regions shouldn’t be on the border
        Any 'O' that is not on the border and it is not connected to an 'O' 
        on the border will be flipped to 'X'.

        Do not return anything, modify board in-place instead.

        type board: List[List[str]]
        rtype: None 
        """
        # using dfs to mark the O region attached to the border
        # the input board must have at least one none empty list
        if not any(board): return

        m,n = len(board),len(board[0])
        borderstack = [ij for x in range(max(m,n)) for ij in [(0,x),(m-1,x),(x,0),(x,n-1)]]
        # dfs iterative version
        while borderstack:
            i,j = borderstack.pop()
            if 0<=i<m and 0<=j<n and board[i][j]=='O':
                # mark the 'O' and check if its connected cells is also 'O'
                board[i][j]='M'
                borderstack.extend([(i-1,j),(i,j-1),(i+1,j),(i,j+1)])

        # the marked O region will be restored as 'O', and others will be flipped as 'X'
        for row in board:
            for j in range(n):
                row[j] = 'XO'[row[j]=='M']

sol=Solution()
board = [['X', 'O', 'X', 'X'], 
        ['X', 'O', 'X', 'X'], 
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']]
print("the previous board is:\n"+'\n'.join([str(r) for r in board]))
sol.solve(board)
print("after Flipping all the O's into 'X's in surrounded region(not connected to the border), the board is:\n",'\n'.join([str(r) for r in board]))