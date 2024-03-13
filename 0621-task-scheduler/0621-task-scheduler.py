from collections import Counter
from heapq import heappush, heappop


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap, min_heap = [], []
        for task, count in counts.items():
            heappush(max_heap, (-count, task, 1))

        time = 1
        while max_heap or min_heap:
            
            while min_heap and time >= min_heap[0][0]:
                next_available, task, count = heappop(min_heap)
                heappush(max_heap, (-count, task, next_available))

            if max_heap:
                count, task, next_available = heappop(max_heap); count *= -1
                count -= 1
                if count > 0:
                    heappush(min_heap, (time + n + 1, task, count))

            if max_heap:
                time += 1
            elif min_heap:
                time = min_heap[0][0]

        return time
