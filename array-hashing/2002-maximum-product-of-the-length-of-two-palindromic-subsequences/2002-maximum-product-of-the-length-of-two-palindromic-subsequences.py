from heapq import heappush, heappop

class Solution:
    def maxProduct(self, s: str) -> int:
        result = [0]
        n = len(s)

        def is_palindrome(array):
            i, j = 0, len(array) - 1
            while i < j:
                if array[i] == array[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        def helper(i, ss1, ss2):
            if i == n:
                if is_palindrome(ss1) and is_palindrome(ss2):
                    result[0] = max(result[0], len(ss1) * len(ss2))
                return

            ss1.append(s[i])
            helper(i + 1, ss1, ss2)
            ss1.pop()

            ss2.append(s[i])
            helper(i + 1, ss1, ss2)
            ss2.pop()

            helper(i + 1, ss1, ss2)

        helper(0, [], [])

        return result[0]
        