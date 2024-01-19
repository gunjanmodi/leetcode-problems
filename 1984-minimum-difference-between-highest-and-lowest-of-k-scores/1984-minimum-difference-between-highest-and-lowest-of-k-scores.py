class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer, i = float('inf'), 0
        
        for j in range(k - 1, len(nums)):
            answer = min(answer, nums[j] - nums[i])
            i += 1
            
        return answer
        