class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        if nums[left] < nums[right]:
             self.binary_search(nums, target, 0, n - 1)

        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        min_index = left

        ans_from_left_part = self.binary_search(nums, target, 0 , min_index - 1)
        ans_from_right_part = self.binary_search(nums, target, min_index, n - 1)

        if ans_from_left_part == -1 and ans_from_right_part == -1:
            return -1
        return ans_from_left_part if ans_from_left_part != -1 else ans_from_right_part

    def binary_search(self, nums, target, left, right):
        while left < right:
            mid = (left + right) >> 1

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1
