class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i, j = 0, len(arr) - 1

        while j - i + 1 > k:
            if abs(arr[j] - x) >= abs(arr[i] - x):
                j -= 1
            else:
                i += 1

        result = []
        for idx in range(i, j + 1):
            result.append(arr[idx])

        return result
        
