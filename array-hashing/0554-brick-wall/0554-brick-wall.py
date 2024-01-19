class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = collections.defaultdict(lambda : 0)
        max_frequency = 0
        
        for line in wall:
            edge = 0
            for i in range(len(line) - 1):
                edge += line[i]
                d[edge] += 1
                max_frequency = max(max_frequency, d[edge])
        
        return len(wall) - max_frequency


        