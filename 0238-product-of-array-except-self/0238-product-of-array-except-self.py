class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]
        result = [1 for _ in range(n)]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result

        