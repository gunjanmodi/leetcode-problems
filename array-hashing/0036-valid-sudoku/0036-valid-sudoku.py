class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        rows_set = [set() for _ in range(9)]
        cols_set = [set() for _ in range(9)]
        grids_set = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(m):
            for j in range(n):
                val = board[i][j]
                x, y = i // 3, j // 3
                if val == '.':
                    continue
                
                if val in rows_set[i] or val in cols_set[j] or val in grids_set[x][y]:
                    return False

                rows_set[i].add(val)
                cols_set[j].add(val)
                grids_set[x][y].add(val)

        return True



        