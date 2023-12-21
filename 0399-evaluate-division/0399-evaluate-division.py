class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        n = len(equations)
        for i in range(n):
            node1, node2 = equations[i]
            graph[node1].append([node2, values[i]])
            graph[node2].append([node1, 1/values[i]])

        def helper(node, target, visited, running_product):
            if node == target:
                return 1
            visited.add(node)
            for child, value in graph[node]:
                if child not in visited:
                    answer = helper(child, target, visited, running_product)
                    if answer > 0:
                        return float(answer * value)
            return -1.000
                    
        def dfs(node, target, running, visited):
            if node == target:
                return running
            for adjacent, multi in graph[node]:
                if adjacent not in visited:
                    visited.add(adjacent)
                    answer = dfs(adjacent, target, running, visited)
                    if answer > 0:
                        return answer * multi
            return -1

        result = [-1 for i in range(len(queries))]

        for i in range(len(queries)):
            node1, node2 = queries[i]
            if node1 not in graph or node2 not in graph:
                continue
            if node1 == node2:
                answer = 1
            else:
                answer = dfs(node1, node2, 1, set())
            result[i] = answer

        return result
        