class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, result, total = 0, float('inf'), 0

        for j in range(len(nums)):

            total += nums[j]

            while total >= target:
                result = min(result, j - i + 1)
                total -= nums[i]
                i += 1

        return result if result != float('inf') else 0