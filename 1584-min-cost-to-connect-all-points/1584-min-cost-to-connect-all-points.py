from heapq import heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        graph = [[] for _ in range(n)]
        min_dist = float('inf')

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                distance = abs(x1-x2) + abs(y1-y2)
                graph[i].append([j, distance])
                graph[j].append([i, distance])
                if min_dist > distance:
                    min_dist = distance
                    point1, point2 = i, j

        min_heap = [(min_dist, point1, point2)]
        visited_edges = set()
        min_cost = 0
        target_count = n
        discovered = set()
        while min_heap and len(discovered) < n:
            distance, node1, node2 = heappop(min_heap)
            if node1 in discovered and node2 in discovered:
                continue
            min_cost += distance
            visited_edges.add((node1, node2))
            discovered.add(node1)
            discovered.add(node2)

            for adjacent, distance in graph[node1]:
                if (node1, adjacent) not in visited_edges and (adjacent, node1) not in visited_edges:
                    heappush(min_heap, (distance, node1, adjacent))

            for adjacent, distance in graph[node2]:
                if (node2, adjacent) not in visited_edges and (adjacent, node2) not in visited_edges:
                    heappush(min_heap, (distance, node2, adjacent))

        return min_cost
        