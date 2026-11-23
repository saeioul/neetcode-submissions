class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Representation first: "." is empty 
        # [[1,2,.],
        #  [1,2,1],
        #  [.,.,1]
        #  ] -> [x][y]

        # For this problem we need to be able to track 
        # rows, columnts and squares. Defaultdict needs no empty check.
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        # We can do it in a single o n2 pass:

        for i in range(0, len(board)):
            for j in range(0, len(board)):

                if board[i][j] == ".":
                    continue

                # Check for repeating numbers
                if (board[i][j] in rows[i] or
                   board[i][j] in cols[j] or
                   board[i][j] in sqrs[( i // 3, j // 3)]):
                   return False

                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                sqrs[( i // 3, j // 3)].add(board[i][j])

        return True

