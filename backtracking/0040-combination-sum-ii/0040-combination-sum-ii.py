class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        candidates.sort()

        def backtrack(i, selection, running_sum):
            if running_sum == target:
                result.append(selection[:])
                return
            
            if i == n or running_sum > target:
                return
                
            selection.append(candidates[i])
            backtrack(i + 1, selection, running_sum + candidates[i])
            
            selection.pop()

            while i + 1 < n and candidates[i] == candidates[i+1]:
                i += 1

            backtrack(i+1, selection, running_sum)

        backtrack(0, [], 0)

        return result
        