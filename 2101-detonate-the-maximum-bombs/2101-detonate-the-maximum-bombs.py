class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]

        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, r2 = bombs[j]
                d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
                if d <= r1:
                    graph[i].append(j)
        
        def dfs(bomb, visited):
            for adjacent in graph[bomb]:
                if adjacent not in visited:
                    visited.add(adjacent)
                    dfs(adjacent, visited)
        
        answer = 0
        for bomb in range(n):
            visited = set([bomb])
            dfs(bomb, visited)
            answer = max(answer, len(visited))
        return answer



        