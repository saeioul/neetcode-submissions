class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # This ruleset allows for O(n2) - with a single scan

        rowDict = defaultdict(set)
        colDict = defaultdict(set)
        boxDict = defaultdict(set)

        for i in range(0, len(board)):
            for j in range(0, len(board)):
            
                cellValue = board[i][j]

                if cellValue == ".":
                    continue
                


                if (cellValue in rowDict[i]
                    or cellValue in colDict[j]
                    or cellValue in boxDict[(i // 3 , j // 3)]):
                    return False

                rowDict[i].add(cellValue)
                colDict[j].add(cellValue)
                boxDict[(i // 3 , j // 3)].add(cellValue)

        return True
        