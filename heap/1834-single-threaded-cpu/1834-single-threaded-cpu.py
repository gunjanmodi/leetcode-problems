class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort(key = lambda x:x[0])
        
        ans, task_queue = [], []
        i, t = 0, tasks[0][0]

        while len(ans) < len(tasks):

            while i < len(tasks) and t >= tasks[i][0]:
                heappush(task_queue, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if not task_queue:
                t = tasks[i][0]
                continue
            
            processing_time, task_id = heappop(task_queue)
            ans.append(task_id)
            t += processing_time
        
        return ans
            