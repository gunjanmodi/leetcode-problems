class Solution:
    def splitString(self, s: str) -> bool:

        def backtrack(s, combination):
            if len(s) == 0:
                return True if len(combination) > 1 else False

            for i in range(len(s)):
                temp = s[:i+1]

                if (len(combination) > 0 and combination[-1] - int(temp) != 1):
                    continue
                    
                combination.append(int(temp))

                if backtrack(s[i+1:], combination):
                    return True

                combination.pop()
            return False

        return backtrack(s, [])
