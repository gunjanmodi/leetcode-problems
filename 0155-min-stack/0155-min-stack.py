class MinStack:

    def __init__(self):
        self._stack = []
        self._min_stack = []

    def isEmpty(self) -> bool:
        return len(self._stack) == 0

    def push(self, val: int) -> None:
        current_min = self.getMin()
        if val < current_min:
            current_min = val
        self._stack.append(val)
        self._min_stack.append(current_min)

    def pop(self) -> None:
        if not self.isEmpty():
            self._stack.pop()
            self._min_stack.pop()

    def top(self) -> int:
        if not self.isEmpty():
            return self._stack[-1]

    def getMin(self) -> int:
        if not self.isEmpty():
            return self._min_stack[-1]
        return float('inf')

        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()