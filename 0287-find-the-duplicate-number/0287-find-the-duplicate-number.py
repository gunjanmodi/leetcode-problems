class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            target_idx = abs(nums[i])
            
            if nums[target_idx] < 0:
                return target_idx
            
            nums[target_idx] = -nums[target_idx]
           
        