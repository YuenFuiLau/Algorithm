class q_combination:

    def __init__(self,dim=2):

        self.board_fragment =  "."*dim
        self.board = [self.board_fragment for i in range(dim)]
        self.combination = []
        self.N = dim
        self.q_count = 0


    def validate_pos(self,board,row_index,col_index):


        for row in range(self.N):

            if board[row][col_index] == "Q":

                return False


        new_row = row_index - 1
        new_col = col_index + 1
        while ( (new_row >= 0) and (new_col < self.N) ):

            if board[new_row][new_col] == "Q":

                return False

            new_row -= 1
            new_col += 1
            

        new_row = row_index - 1
        new_col = col_index - 1
        while ( (new_row >= 0) and (new_col >= 0) ):

            if board[new_row][new_col] == "Q":

                return False

            new_row -= 1
            new_col -= 1

        
        return True
        

    def count_combination(self,board,row = 0):

        if row == self.N:
                
            self.combination.append(board)

            return


        for j in range(self.N):
            

            if self.validate_pos(board[:],row,j):

                board[row] = board[row][:j] + "Q" + board[row][j+1:]

            else:

                continue
                                                      

            self.count_combination(board[:],row+1)

            board[row] = board[row][:j] + "." + board[row][j+1:]


    def Print_Board(self):

        for board in self.combination:

            print("--------------------------------------------")

            for i in range(self.N):

                for j in range(self.N):

                    print(board[i][j],"\0\0\0",end=" ")

                print("\n")

            print("--------------------------------------------")
            

    def __count__(self):

        self.count_combination(self.board[:])

        return len(self.combination)



obj = q_combination(8)
ans = obj.__count__()
obj.Print_Board()
a = obj.combination

