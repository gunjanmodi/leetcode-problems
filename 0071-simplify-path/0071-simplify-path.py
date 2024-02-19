class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for ch in path.split('/'):
            if not ch or ch == '.':
                continue
            elif ch == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)

        return f'/{"/".join(stack)}'
        