from collections import Counter, deque
from heapq import heappush, heappop


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap, queue = [], deque()
        for task, count in counts.items():
            heappush(max_heap, (-count, task, 1))

        time = 1
        while max_heap or queue:
            
            while queue and time >= queue[0][0]:
                next_available, task, count = queue.popleft()
                heappush(max_heap, (-count, task, next_available))

            if max_heap:
                count, task, next_available = heappop(max_heap); count *= -1
                count -= 1
                if count > 0:
                    queue.append((time + n + 1, task, count))

            if max_heap:
                time += 1
            elif queue:
                time = queue[0][0]

        return time
