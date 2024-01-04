class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        answer = []

        for i in range(n):
            answer.append('1' if nums[i][i] == '0' else '0')
        
        return ''.join(answer)
      
