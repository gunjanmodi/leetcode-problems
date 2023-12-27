class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        
        def backtrack(i, selection):
            if i == n:
                result.append(selection[:])
                return
            else:
                backtrack(i+1, selection)
                selection.append(nums[i])
                backtrack(i+1, selection)
                selection.pop()

        backtrack(0, [])
        return result



        