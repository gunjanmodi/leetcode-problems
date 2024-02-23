class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        i, total, result = 0, 0, 0
        for j in range(len(nums)):
            total += nums[j]
            
            while ((j - i + 1) * nums[j]) - total  > k:
                total -= nums[i]
                i += 1

            result = max(result, j - i + 1)
           
        return result
