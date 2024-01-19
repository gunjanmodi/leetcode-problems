class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def sorting_function(x, y):
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1

        nums_str = list(map(lambda x: str(x), nums))
        nums_str.sort(key = cmp_to_key(sorting_function), reverse=True)
        return ''.join(nums_str).lstrip('0') or '0'