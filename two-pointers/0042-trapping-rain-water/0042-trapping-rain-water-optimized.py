class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        trapped_watter = [0 for _ in range(n)]
        result, max_so_far = 0, 0

        for i in range(n-1, -1, -1):
            trapped_watter[i] = max(max_so_far - height[i], 0)
            max_so_far = max(max_so_far, height[i])

        max_so_far = 0
        for i in range(n):
            result += min(trapped_watter[i], max(max_so_far - height[i], 0))
            max_so_far = max(max_so_far, height[i])

        return result
