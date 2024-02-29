class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        while top < bottom:
            mid = (top + bottom) >> 1
            if matrix[mid][n-1] < target:
                top = mid + 1
            else:
                bottom = mid

        if top == m:
            return False
        
        row = top
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) >> 1
            if matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return True if matrix[row][left] == target else False

        