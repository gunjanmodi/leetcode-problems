class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i, j = 0, 0
        m, n = len(pushed), len(popped)
        while i < m:
            while i < m and pushed[i] != popped[j]:
                stack.append(pushed[i])
                i += 1
            
            while i < m and j < n and pushed[i] == popped[j]:
                i += 1
                j += 1

            while stack and j < n and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        while stack:
            top = stack.pop()
            if popped[j] == top:
                j += 1
        
        return j == n
