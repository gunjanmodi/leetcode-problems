class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def check_palindrome(s):
            i, j = 0, len(s) - 1
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            return i >= j

        def backtrack(s, combination):
            
            if len(s) == 0:
                result.append(combination[:])
                return

            for i in range(1, len(s) + 1):
                partioned_s = s[:i]
                if not check_palindrome(partioned_s):
                    continue
                
                combination.append(partioned_s)
                backtrack(s[i:], combination)
                combination.pop()

        backtrack(s, [])

        return result
        


    