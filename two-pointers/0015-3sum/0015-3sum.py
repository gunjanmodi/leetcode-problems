class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result, i, n = [], 0, len(nums)
        
        while i < n:

            while i > 0 and i < n and nums[i] == nums[i - 1]:
                i += 1

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    while j + 1 < n and nums[j] == nums[j - 1]:
                        j += 1

                    while k - 1 >= 0 and j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif total < 0:
                    j += 1


                elif total > 0:
                    k -= 1

            i += 1

        return result
