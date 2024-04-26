from collections import Counter
from heapq import heappop, heappush, heapify

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_heap = [(-count, char) for char, count in counts.items()]
        heapify(max_heap)
        result = []
        parked_count, parked_char = 0, ''

        while max_heap:
            count, char = heappop(max_heap)
            result.append(char)

            if parked_count < 0:
                heappush(max_heap, (parked_count, parked_char))

            parked_count, parked_char = count, char
            parked_count += 1

        if len(result) != len(s):
            return ""

        return ''.join(result)
