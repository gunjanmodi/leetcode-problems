class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        n = len(colors)
        indegrees = {i: 0 for i in range(n)}
        colors_dict = {i: colors[i] for i in range(n)}
        unique_colors = list(set(colors))

        for node1, node2 in edges:
            graph[node1].append(node2)
            indegrees[node2] += 1

        queue = collections.deque()
        for node, count in indegrees.items():
            if count == 0:
                queue.append(node)

        topological_order = []
        while queue:
            node = queue.popleft()
            topological_order.append(node)

            for adjacent in graph[node]:
                indegrees[adjacent] -= 1
                if indegrees[adjacent] == 0:
                    queue.append(adjacent)

        if len(topological_order) != n:
            return -1
            
        dp = []
        for i in range(n):
            dp.append({color: 0 for color in unique_colors})

        answer = 0
        for node in reversed(topological_order):
            for color in unique_colors:
                max_count = 0
                for adjacent in graph[node]:
                    max_count = max(max_count, dp[adjacent][color])
                dp[node][color] = max_count
            dp[node][colors_dict[node]] += 1
            answer = max(answer, dp[node][colors_dict[node]])

        return answer
