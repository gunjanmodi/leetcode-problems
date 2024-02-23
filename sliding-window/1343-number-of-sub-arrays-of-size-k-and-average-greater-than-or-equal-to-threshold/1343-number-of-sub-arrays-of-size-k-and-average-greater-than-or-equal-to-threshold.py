class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i, total, result = 0, 0, 0
        for j in range(len(arr)):
            total += arr[j]
            if j - i + 1 == k:
                if total / k >= threshold:
                    result += 1
                total -= arr[i]
                i += 1
        return result

            
        