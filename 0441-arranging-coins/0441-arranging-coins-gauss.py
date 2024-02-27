class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        result = 1

        while left < right:
            mid = (left + right) >> 1
            
            if (mid + 1) * (mid/2) <= n:
                result = mid
                left = mid + 1
            else:
                right = mid
        return result
