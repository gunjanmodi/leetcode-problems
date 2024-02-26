class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            
            mid = left + (right - left) // 2
            
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
                
        if nums[left] >= target:
            return left
        return len(nums)
    