from functools import cmp_to_key

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def sorter(x, y):
            if len(x) < len(y):
                return -1
            elif len(x) > len(y):
                return 1
            else:
                if x < y:
                    return -1
                elif x < y:
                    return 1
                else:
                    return 0

        nums.sort(key = cmp_to_key(sorter))
        return nums[len(nums) - k]

