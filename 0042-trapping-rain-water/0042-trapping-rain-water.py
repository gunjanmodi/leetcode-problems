class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        trapped_watter_right = [0 for _ in range(n)]
        trapped_watter_left =  [0 for _ in range(n)]
        
        result = 0
        max_so_far = 0
        
        for i in range(n-1, -1, -1):
            trapped_watter_right[i] = max(max_so_far - height[i], 0)
            max_so_far = max(max_so_far, height[i])

        max_so_far = 0
        for i in range(n):
            trapped_watter_left[i] = max(max_so_far - height[i], 0)
            max_so_far = max(max_so_far, height[i])

        for i in range(n):
            result += min(trapped_watter_right[i], trapped_watter_left[i])
        return result
