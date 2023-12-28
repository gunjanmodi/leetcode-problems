class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(idx, selection):
            if len(selection) == k:
                result.append(selection[:])
                return
            for i in range(idx, n+1):
                selection.append(i)
                backtrack(i + 1, selection)
                selection.pop()

        backtrack(1, [])

        return result