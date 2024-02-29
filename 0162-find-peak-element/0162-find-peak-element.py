class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1

        def condition_func(idx):
            if idx == 0:
                return True if nums[idx] < nums[idx + 1] else False
            else:
                if nums[idx] < nums[idx + 1] and nums[idx - 1] < nums[idx + 1]:
                    return True
                else:
                    return False

        while left < right:
            mid = (left + right) >> 1
            
            if condition_func(mid):
                left = mid + 1
            else:
                right = mid
                
        return left
        