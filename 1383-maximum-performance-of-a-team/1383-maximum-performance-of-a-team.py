class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        enignners = list(zip(efficiency, speed))
        enignners.sort(key = lambda x: x[0], reverse=True)
        min_heap = []
        current_speed, answer = 0, 0
        modulo = 10**9 + 7
        for i in range(k - 1):
            heappush(min_heap, enignners[i][1])
            current_speed += enignners[i][1]
            answer = max(answer, current_speed * enignners[i][0])

        for i in range(k - 1, n):
            heappush(min_heap, enignners[i][1])
            current_speed += enignners[i][1]
            answer = max(answer, current_speed * enignners[i][0])
            min_speed_so_far = heappop(min_heap)
            current_speed -= min_speed_so_far

        return answer % modulo
    