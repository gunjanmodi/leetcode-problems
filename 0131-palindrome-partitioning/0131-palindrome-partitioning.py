class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s) - 1

        def check_palindrome(s):
            i, j = 0, len(s) - 1
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            return i >= j

        def helper(inps, combination):
            
            if inps == '' or len(inps) == 0:
                result.append(combination[:])
                return

            for i in range(1, len(inps) + 1):
                temp = inps[:i]
                if not check_palindrome(temp):
                    continue
                
                combination.append(temp)
                helper(inps[i:], combination)
                combination.pop()

        helper(s, [])

        return result
        


    