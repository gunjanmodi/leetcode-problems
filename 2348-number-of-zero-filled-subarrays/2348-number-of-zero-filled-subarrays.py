class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zero_subarrays_length = []
        i, j, result = 0, 0, 0
        while i < len(nums):
            if nums[i] != 0:
                i += 1
            else:
                j = i
                while i < len(nums) and nums[i] == 0:
                    i += 1
                zero_subarrays_length.append(i - j)
        
        for count in zero_subarrays_length:
            result += count +  ( count * (count-1) // 2)
        return result
                
            
        