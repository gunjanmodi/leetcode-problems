class Solution:
    def minSwaps(self, s: str) -> int:
        opening = len(s) // 2
        stack, count = 0, 0

        for i in range(len(s)):
        
            if s[i] == '[' and opening > 0:
                opening -= 1
                stack += 1
        
            elif s[i] == ']':
                if stack > 0:
                    stack -= 1
                else:
                    opening -= 1
                    stack += 1
        
        return stack

