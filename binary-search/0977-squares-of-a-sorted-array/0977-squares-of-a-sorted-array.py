class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_array = [0 for _ in range(len(nums))]
        i = len(nums) - 1
        left = 0
        right = len(nums) - 1
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                sorted_array[i] = nums[right] * nums[right]
                right -= 1
            else:
                sorted_array[i] = nums[left] * nums[left]
                left += 1
            i -= 1
        return sorted_array 
        