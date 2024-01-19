class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = n + 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = max_val
                
        for i in range(n):
            num = abs(nums[i])
            
            if num > n:
                continue

            if nums[num - 1] > 0:
                nums[num - 1] *= -1

        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1