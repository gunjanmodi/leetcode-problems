class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [-1]
        ngr = {}

        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]
            while stack and stack[-1] <= num:
                stack.pop()
            
            if len(stack) == 0:
                ngr[num] = -1
            else:
                ngr[num] = stack[-1]
            stack.append(num)

        return [ngr[num] for num in nums1]
