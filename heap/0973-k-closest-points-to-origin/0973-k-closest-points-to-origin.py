class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            distance = x**2 + y**2
            heappush(max_heap, (-distance, (x, y)))

            if len(max_heap) > k:
                heappop(max_heap)

        result = []
        for distance, point in max_heap:
            result.append([point[0], point[1]])
        
        return result
        