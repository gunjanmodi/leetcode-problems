class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        NON_VISITED, SAFE, INSIDE_RECURSION = 0, 1, 2
        n = len(graph)
        result = []
        color = [NON_VISITED for _ in range(n)]

        def helper(node):
            if color[node] == INSIDE_RECURSION:
                return False

            if color[node] == SAFE: # This condition added just to prevent TLE for some test cases.
                return True # Code is correct without this too

            color[node] = INSIDE_RECURSION

            for adjacent in graph[node]:
                if not helper(adjacent):
                    return False

            color[node] = SAFE
            return True

        for node in range(n):
            if color[node] == SAFE or helper(node):
                result.append(node)

        return result
