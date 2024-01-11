from collections import Counter
from heapq import heappop, heappush

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap, result = [], []
        counter = Counter(nums)

        for key, value in counter.items():
            heappush(max_heap, (-value, key))


        for _ in range(k):
            counter, num = heappop(max_heap)
            result.append(num)

        return result
