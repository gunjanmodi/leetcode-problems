class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reversed_graph = collections.defaultdict(list)
        outdegrees = collections.defaultdict(lambda : 0)
        queue = collections.deque()

        for node in range(n):
            for adjacent in graph[node]:
                reversed_graph[adjacent].append(node)
                outdegrees[node] += 1
            if outdegrees[node] == 0:
                queue.append(node)

        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for adjacent in reversed_graph[node]:
                outdegrees[adjacent] -= 1

                if outdegrees[adjacent] == 0:
                    queue.append(adjacent)

        return sorted(result)
