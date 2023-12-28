class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        candidates.sort()

        def backtrack(i, selection, running_sum):
            if i == n or running_sum > target:
                return
            elif running_sum == target:
                result.append(selection[:])
                return
            else:
                selection.append(candidates[i])
                backtrack(i, selection, running_sum + candidates[i])

                selection.pop()
                backtrack(i + 1, selection, running_sum)

        backtrack(0, [], 0)

        return result