class Solution:
    def totalNQueens(self, n: int) -> int:

        total = [0]
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols_set = set()
        positive_diag = set()
        negative_diag = set()

        def backtrack(r):
                
            if r == n:
                total[0] += 1
                return

            for c in range(n):
                if c in cols_set or r + c in positive_diag or r - c in negative_diag:
                    continue
                
                board[r][c] = 'Q'
                cols_set.add(c)
                positive_diag.add(r + c)
                negative_diag.add(r - c)

                backtrack(r + 1)

                board[r][c] = '.'
                cols_set.remove(c)
                positive_diag.remove(r + c)
                negative_diag.remove(r - c)

        backtrack(0)            

        return total[0]
