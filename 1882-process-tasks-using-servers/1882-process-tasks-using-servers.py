from heapq import heappop, heappush, heapify

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        server_pool, execution_queue, ans = [], [], []

        for server_id, server_weight in enumerate(servers):
            server_pool.append((server_weight, server_id))
        heapify(server_pool)

        t, i = 0, 0
        while i < len(tasks):
            while execution_queue and execution_queue[0][0] <= t:
                available_time, server_id = heappop(execution_queue)
                heappush(server_pool, (servers[server_id], server_id))

            while server_pool and t >= i and i < len(tasks):
                server_weight, server_id = heappop(server_pool)
                ans.append(server_id)
                heappush(execution_queue, (t + tasks[i], server_id))
                i += 1

            if not server_pool:
                t = execution_queue[0][0]
            else:
                t += 1

        return ans
