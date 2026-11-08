class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Per sudoku rules, store seen elements per:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        sqrMap = defaultdict(set)

        #Now we can just iterate the provided list of lists
        sizeOfList = len(board) # should be 9

        for row in range(0, sizeOfList):
            for column in range(0, sizeOfList):
                if board[row][column] == ".":
                    continue
                if (board[row][column] in rowMap[row]
                    or board[row][column] in colMap[column]
                    or board[row][column] in sqrMap[row // 3, column // 3]):
                    return False

                rowMap[row].add(board[row][column])
                colMap[column].add(board[row][column])
                sqrMap[row // 3, column // 3].add(board[row][column])

        return True


