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

                    if partition[j] == 0:
                        break


        backtrack(0)

        return answer[0]