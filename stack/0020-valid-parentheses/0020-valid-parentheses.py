class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_brackets = {')', '}', ']'}
        brackets_pairs = {'(': ')', '{': '}', '[': ']'}

        for ch in s:
            
            if ch in closing_brackets:
                if stack and brackets_pairs[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(ch)

        return True if len(stack) == 0 else False
            
        