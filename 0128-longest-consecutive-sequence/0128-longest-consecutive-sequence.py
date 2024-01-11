class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        result = 0

        for i in range(len(nums)):
            if nums[i] - 1 in s:
                continue
                
            j = 1
            while nums[i] + j in s:
                j += 1
            result = max(result, j)
            
        return result

        