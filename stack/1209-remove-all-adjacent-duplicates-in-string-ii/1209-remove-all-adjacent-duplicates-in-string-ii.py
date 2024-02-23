class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [[s[0], 1]]
        for i in range(1, len(s)):
            ch, counter = s[i], 1
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, counter])
                
        return "".join([ch * count for ch, count in stack ])
