from heapq import heappop, heappush

class FreqStack:

    def __init__(self):
        self.max_heap = []
        self.d = {}
        self.count = 0

    def push(self, val: int) -> None:
        self.count += 1
        self.d[val] = self.d.get(val, 0) + 1
        heappush(self.max_heap, (-self.d[val], -self.count, val))

    def pop(self) -> int:
        freq, idx, num = heappop(self.max_heap)
        self.d[num] -= 1
        return num
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()