class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def days_to_eat_banana(speed):
            total = 0
            for pile in piles:
                total += math.ceil(pile / speed)
                
            return total

        while left < right:
            
            mid = (left + right) >> 1
            
            if days_to_eat_banana(mid) > h:
                left = mid + 1
            else:
                right = mid

        return left