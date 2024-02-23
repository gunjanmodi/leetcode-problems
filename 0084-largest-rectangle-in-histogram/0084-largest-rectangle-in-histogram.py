class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = float('-inf')
        smaller_left = self.next_smaller_left(heights, n)
        smaller_right = self.next_smaller_right(heights, n)

        for i in range(n):
            left_expan = i - smaller_left[i] - 1
            right_exapan = smaller_right[i] - i - 1
            area = (left_expan + right_exapan + 1) * heights[i]
            max_area = max(max_area, area)
        return max_area

    def next_smaller_left(self, nums, n):
        stack = []
        result = [-1 for _ in range(n)]
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if len(stack) == 0:
                result[i] = -1
            elif nums[stack[-1]] < nums[i]:
                result[i] = stack[-1]
            
            stack.append(i)
        return result

    def next_smaller_right(self, nums, n):
        stack = []
        result = [-1 for _ in range(n)]
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if len(stack) == 0:
                result[i] = n
            elif nums[stack[-1]] < nums[i]:
                result[i] = stack[-1]
            
            stack.append(i)

        return result
