from heapq import heappush, heappop


class SeatManager:

    def __init__(self, n: int):
        self.counter = 0
        self.min_heap = []

    def reserve(self) -> int:
        if self.min_heap:
            return heappop(self.min_heap)
        else:
            self.counter += 1
            return self.counter

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.min_heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
