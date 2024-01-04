class Solution:
    def totalNQueens(self, n: int) -> int:

        total = [0]

        def backtrack(row, col, board, queen, combination):
            if len(combination) == n:
                total[0] += 1
                return

            for i in range(row, n):
                for j in range(n):
                    if len(board[i][j]) == 0:
                        self.choose(i, j, queen, combination, board, n)
                        backtrack(i, j, board, queen + 1, combination)
                        self.unchoose(i, j, queen, combination, board, n)

        board = [[[] for _ in range(n)] for _ in range(n)]
        for column in range(n):
            combination = []
            self.choose(0, column, 1, combination, board, n)
            backtrack(0, column, board, 2, combination)
            self.unchoose(0, column, 1, combination, board, n)

        return total[0]


    def choose(self, i, j, queen, combination, board, n):
        combination.append((i, j))
        board[i][j].append(queen)
        # queen will be added to 8 directions
        # Add queen to Top Left 
        r, c = i - 1, j - 1 
        while r >= 0 and c >= 0:
            board[r][c].append(queen)
            r -= 1
            c -= 1
        # Add queen to Top
        r, c = i - 1, j
        while r >= 0:
            board[r][c].append(queen)
            r -= 1
        # Add queen to Top Right
        r, c = i - 1, j + 1 
        while r >= 0 and c < n:
            board[r][c].append(queen)
            r -= 1
            c += 1
        # Add queen to left
        r, c = i, j - 1
        while c >= 0:
            board[r][c].append(queen)
            c -= 1
        # Add queen to right
        r, c = i, j + 1 
        while c < n:
            board[r][c].append(queen)
            c += 1
        # Add queen to bottom Left
        r, c = i + 1, j - 1 
        while r < n and c >= 0:
            board[r][c].append(queen)
            r += 1
            c -= 1
        # Add queen to bottom
        r, c = i + 1, j
        while r < n:
            board[r][c].append(queen)
            r += 1
        # Add queen to bottom Right
        r, c = i + 1, j + 1 
        while r < n and c < n:
            board[r][c].append(queen)
            r += 1
            c += 1
    
    def unchoose(self, i, j, queen, combination, board, n):
        combination.pop()
        board[i][j].pop()
        # queen will be removed to 8 directions
        # Remove queen from Top Left 
        r, c = i - 1, j - 1 
        while r >= 0 and c  >= 0:
            board[r][c].pop()
            r -= 1
            c -= 1
        # Remove queen from Top
        r, c = i - 1, j
        while r >= 0:
            board[r][c].pop()
            r -= 1
        # Remove queen from Top Right
        r, c = i - 1, j + 1 
        while r >= 0 and c < n:
            board[r][c].pop()
            r -= 1
            c += 1
        # Remove queen from left
        r, c = i, j - 1
        while c >= 0:
            board[r][c].pop()
            c -= 1
        # Remove queen from right
        r, c = i, j + 1 
        while c < n:
            board[r][c].pop()
            c += 1
        # Remove queen from bottom Left
        r, c = i + 1, j - 1 
        while r < n and c >= 0:
            board[r][c].pop()
            r += 1
            c -= 1
        # Remove queen from bottom
        r, c = i + 1, j
        while r < n:
            board[r][c].pop()
            r += 1
        # Remove queen from bottom Right
        r, c = i + 1, j + 1 
        while r < n and c < n:
            board[r][c].pop()
            r += 1
            c += 1
