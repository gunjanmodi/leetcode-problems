from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        i, result = 0, []

        for j in range(len(nums)):
            while queue and queue[-1] < nums[j]:
                queue.pop()
            queue.append(nums[j])

            if j - i + 1 == k:
                result.append(queue[0])

                if nums[i] == queue[0]:
                    queue.popleft()
                i += 1

        return result
    