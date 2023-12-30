class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        rows_range, cols_range = set(range(m)), set(range(n))

        def backtrack(i, j, k, visited):
            if k >= len(word):
                return True
            if i not in rows_range or j not in cols_range or (i, j) in visited or word[k] != board[i][j]:
                return False

            visited.add((i, j))

            top = backtrack(i - 1, j, k + 1, visited)
            right = backtrack(i, j + 1, k + 1, visited)
            bottom = backtrack(i + 1, j, k + 1, visited)
            left = backtrack(i, j - 1, k + 1, visited)

            visited.remove((i, j))
            return top or right or bottom or left
        

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0, set()):
                        return True

        return False

        