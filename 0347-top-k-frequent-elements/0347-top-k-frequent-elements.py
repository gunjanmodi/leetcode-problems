from collections import Counter, defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        counter = Counter(nums)

        for key, value in counter.items():
            bucket[value].append(key)

        result = []
        i = len(bucket) - 1

        while i >= 0 and len(result) < k:
            if bucket[i]:
                for num in bucket[i]:
                    result.append(num)
            i -= 1

        return result

        