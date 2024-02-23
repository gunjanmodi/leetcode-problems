class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        current_min = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            while stack and num >= stack[-1][0]:
                stack.pop()
            if stack and num > stack[-1][1]:
                return True
            stack.append([num, current_min])
            current_min = min(num, current_min)
        return False
