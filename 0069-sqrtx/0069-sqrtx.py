class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        
        while left < right:
            mid = (left + right) >> 1
            
            if mid * mid < x:
                left = mid + 1
            else:
                right = mid
        
        return left if left * left == x else left - 1