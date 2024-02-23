from heapq import heappop, heappush

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap, result = [], []

        for num in arr:
            heappush(min_heap, (abs(num - x), num))

        for _ in range(k):
            __, num = heappop(min_heap)
            result.append(num)

        result.sort()

        return result
  
