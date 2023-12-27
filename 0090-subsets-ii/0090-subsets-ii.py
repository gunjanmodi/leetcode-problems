class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        def backtrack(i, selection):
            if i == n:
                result.append(selection[:])
                return
            selection.append(nums[i])
            backtrack(i + 1, selection)

            selection.pop()

            while i+1 < n and nums[i] == nums[i+1]:
                i += 1

            backtrack(i + 1, selection)

        backtrack(0, [])
        return result
        