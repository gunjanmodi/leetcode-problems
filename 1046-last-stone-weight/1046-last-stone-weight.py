class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapify(max_heap)

        while len(max_heap) > 1: 
            y = heappop(max_heap);y *= -1
            x = heappop(max_heap);x *= -1
            heappush(max_heap, (y - x) * -1)
        
        result = heappop(max_heap); result *= -1
        return result
