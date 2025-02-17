def is_safe (board,roe,col,N):

    for I in range(row):
        if board[I]==col or \
        board[I]-1== col - row or \
        board[I]+1== col+ row:
            return False
        return True
    
    def solve_n_queens(board,row ,N):
        if row == N:
            print_solution (board,N)
            return
        
        for col in range(N):
            if is_safe(board,row,col,N):
                board[row]=col
                solve_n_queens(*board,row+1,N)
                board[row]=-1
    def print_solution(board,N):
        print ("\nSolution :")
        for i in range(N):
            row = ['.']*N
            row[board[i]]='Q'
            print("".join(row))
            print("\n"+"_"*(2*N))

    def n_qeens(N):
        board =[-1]*N
        solve_n_queens(board,0,N)
        
    
        