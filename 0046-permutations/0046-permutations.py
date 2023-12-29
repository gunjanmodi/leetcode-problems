class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        desired_size = len(nums)

        def backtrack(choice_nums, permutation):
            
            if len(permutation) == desired_size:
                result.append(permutation[:])
                return
            
            for i in range(len(choice_nums)):
                next_choices = choice_nums[:i] + choice_nums[i+1:]
                permutation.append(choice_nums[i])
                backtrack(next_choices, permutation)
                permutation.pop()
        
        backtrack(nums, [])
        
        return result
        