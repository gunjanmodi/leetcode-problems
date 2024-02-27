class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        result = 1
        def can_be_answer(num):
            remaining = n
            for current in range(num, 0, -1):
                remaining -= current
                if remaining < 0:
                    return False
            return True

        while left < right:
            mid = (left + right) >> 1
            if can_be_answer(mid):
                result = mid
                left = mid + 1
            else:
                right = mid
        return result
