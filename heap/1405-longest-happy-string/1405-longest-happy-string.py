from heapq import heappop, heappush, heapify

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapify(max_heap)
        result = []

        while max_heap:
            count, char = heappop(max_heap); count *= -1
            if count == 0:
                break
            if result and result[-1] == char and max_heap:
                second_count, second_char = heappop(max_heap); second_count *= -1
                if second_count == 0:
                    break
                result.append(second_char)
                second_count -= 1
                heappush(max_heap, (-second_count, second_char))
                heappush(max_heap, (-count, char))
            else:
                use_char = min(2, count)
                for _ in range(use_char):
                    result.append(char)
                count -= use_char
                heappush(max_heap, (-count, char))

        return ''.join(result)
        