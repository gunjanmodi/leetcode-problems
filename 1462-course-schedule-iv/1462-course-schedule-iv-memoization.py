class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        dep = {node: set() for node in range(numCourses)}

        for node1, node2 in prerequisites:
            dep[node2].add(node1)

        n = len(queries)
        memo = {}

        result = [False for _ in range(n)]

        def dfs(parent, node) -> bool:
            key = (parent, node)
            if key in memo:
                return memo[key]
            if parent in dep[node]:
                memo[key] = True
            else:
                for adj in dep[node]:
                    if dfs(parent, adj):
                        return True
                memo[key] = False
            return memo[key]

        for i in range(n):
            node1, node2 = queries[i]
            if dfs(node1, node2):
                result[i] = True

        return result
