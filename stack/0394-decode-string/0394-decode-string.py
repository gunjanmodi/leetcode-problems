class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_string = ''
        for ch in s:
            if ch == '[':
                stack.append(current_string)
                stack.append(current_num)
                current_string = ''
                current_num = 0
            elif ch == ']':
                num = stack.pop()
                prevString = stack.pop()
                current_string = prevString + num * current_string
            elif ch.isdigit():
                current_num = current_num * 10 + int(ch)
            else:
                current_string += ch
                
        return current_string