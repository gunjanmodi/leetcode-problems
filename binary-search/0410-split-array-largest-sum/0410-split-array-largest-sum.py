class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = 0, sum(nums)

        def no_of_partitions(total):
            current_total = 0
            count = 0
            for num in nums:
                if num > total:
                    return float('inf')
                current_total += num
                if current_total > total:
                    count += 1
                    current_total = num
                elif current_total == total:
                    count += 1
                    current_total = 0
            if current_total > 0:
                count += 1
            return count

        while left < right:
            mid = (left + right) >> 1
            if no_of_partitions(mid) > k:
                left = mid + 1
            else:
                right = mid

        return left



        