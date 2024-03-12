class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left, right = 0, n - 1

        while left < right:

            while left < right and nums[left] == nums[left+1]:
                left += 1

            while left < right and nums[right] == nums[right-1]:
                right -= 1

            mid = (left + right) >> 1
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        min_index = left
        
        exists_in_left_part = self.binary_search(nums, target, 0 , min_index - 1)
        exists_in_right_part = self.binary_search(nums, target, min_index, n - 1)
        
        return exists_in_left_part or exists_in_right_part

    def binary_search(self, nums, target, left, right):

        while left < right:
            mid = (left + right) >> 1

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return True if nums[left] == target else False
        