class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        desired_sum = total // k
        nums.sort(reverse=True)
        partition = [0 for _ in range(k)]
        answer = [False]

        def backtrack(i):

            if i == len(nums):
                wrong_answer = False
                for value in partition:
                    if value != desired_sum:
                        wrong_answer = True
                        break
                if not wrong_answer:
                    answer[0] = True
                return
            
            for j in range(k):
                if partition[j] + nums[i] <= desired_sum:
                    partition[j] += nums[i]
                    backtrack(i + 1)
                    partition[j] -= nums[i]

                    # Important line, otherwise function will give TLE
                    if partition[j] == 0:
                        break

                    """
                    Explanation:
                    If subSets[j] = 0, it means this is the first time adding values to that subset.
                    If the backtrack search fails when adding the values to subSets[j] and subSets[j] remains 0, it will also fail for all subSets from subSets[j+1:].
                    Because we are simply going through the previous recursive tree again for a different j+1 position.
                    So we can effectively break from the for loop or directly return False.
				    """


        backtrack(0)

        return answer[0]
