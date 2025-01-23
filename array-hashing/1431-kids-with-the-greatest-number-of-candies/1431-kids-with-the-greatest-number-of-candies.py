class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False for _ in range(len(candies))]
        max_candies = max(candies)

        for i in range(len(candies)):
            updated_candies = candies[i] + extraCandies
            if updated_candies >= max_candies:
                result[i] = True
                
        return result
