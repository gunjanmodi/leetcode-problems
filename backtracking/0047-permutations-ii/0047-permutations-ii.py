class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        desired_length = len(nums)
        nums.sort()

        def backtrack(choice_nums, permutation):
            if len(permutation) == desired_length:
                result.append(permutation[:])
                return
            
            for i in range(len(choice_nums)):
                
                if i > 0 and choice_nums[i-1] == choice_nums[i]: # handles duplication
                    continue 

                next_choices = choice_nums[:i] + choice_nums[i+1:]
                permutation.append(choice_nums[i])
                backtrack(next_choices, permutation)
                permutation.pop()

        backtrack(nums, [])

        return result
        