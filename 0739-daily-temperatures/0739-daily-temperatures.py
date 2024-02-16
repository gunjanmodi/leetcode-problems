class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, n = [], len(temperatures)
        result = [0 for _ in range(n)]
        for i in range(n-1, -1, -1):
            
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if stack and temperatures[stack[-1]] > temperatures[i]:
                result[i] = stack[-1] - i

            stack.append(i)

        return result
