class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1 for _ in range(n)]
        curr = 1

        for i in range(n):
            result[i] *= curr
            curr *= nums[i]

        curr = 1
        for i in range(n-1, -1, -1):
            result[i] *= curr
            curr *= nums[i]
            
        return result
