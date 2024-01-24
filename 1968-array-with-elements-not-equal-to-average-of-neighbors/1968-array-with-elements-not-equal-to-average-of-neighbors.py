class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 1, 0
        for i in range(1, n - 1):
            if 2 * nums[i] == nums[i - 1] + nums[i + 1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

        for i in range(n-2, 0, -1):
            if 2 * nums[i] == nums[i - 1] + nums[i + 1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]

        return nums
