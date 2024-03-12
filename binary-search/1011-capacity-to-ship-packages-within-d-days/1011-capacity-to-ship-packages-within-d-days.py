class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_weight = sum(weights)
        left, right = 0, total_weight
        result = total_weight

        def number_of_days_taken(capacity):
            current_cap, days_taken = 0, 0

            for weight in weights:

                if weight > capacity:
                    return float('inf')

                current_cap += weight

                if current_cap > capacity:
                    days_taken += 1
                    current_cap = weight
                elif current_cap == capacity:
                    days_taken += 1
                    current_cap = 0
            if current_cap > 0:
                days_taken += 1
            return days_taken

        while left < right:
            mid = (left + right) >> 1
            days_taken = number_of_days_taken(mid)
            if days_taken <= days:
                result = mid
                right = mid
            else:
                left = mid + 1 
                
        return result
        