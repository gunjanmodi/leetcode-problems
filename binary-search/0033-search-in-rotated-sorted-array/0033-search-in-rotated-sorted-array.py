class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        if nums[left] < nums[right]:
            return self.binary_search(nums, target, 0, n - 1)

        min_index = self.find_min_index(nums, left, right)

        if nums[0] <= target <= nums[min_index - 1]:
            return self.binary_search(nums, target, 0 , min_index - 1)
        else:
            return self.binary_search(nums, target, min_index, n - 1)

    def find_min_index(self, nums, left, right):
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left

    def binary_search(self, nums, target, left, right):
        while left < right:
            mid = (left + right) >> 1

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1
