class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        indegrees = {node: 0 for node in range(n)}
        result = []
        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1

        queue = collections.deque()
        for node, count in indegrees.items():
            if count == 0:
                queue.append(node)

        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for adjacent in graph[node]:
                indegrees[adjacent] -= 1
                if indegrees[adjacent] == 0:
                    queue.append(adjacent)

        return result if len(result) == n else []
