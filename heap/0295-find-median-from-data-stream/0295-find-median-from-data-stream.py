[0,2,6,6,8,10]
class MedianFinder:

    def __init__(self):
        self.max_heap, self.min_heap = [], []
        
    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -num)
        self.rebalance()

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        elif self.max_heap and self.min_heap:
            return min(-self.max_heap[0], self.min_heap[0])
        else:
            return -self.max_heap[0]

    def rebalance(self):
        
        if len(self.max_heap) - len(self.min_heap) > 1:
            num = heappop(self.max_heap)
            heappush(self.min_heap, -num)

        if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            max_heap_el = heappop(self.max_heap)
            min_heap_el = heappop(self.min_heap)
            heappush(self.min_heap, -max_heap_el)
            heappush(self.max_heap, -min_heap_el)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()