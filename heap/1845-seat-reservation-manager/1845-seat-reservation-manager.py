from heapq import heappush, heappop, heapify
class SeatManager:

    def __init__(self, n: int):
        self.capacity = n
        self.min_heap = [i for i in range(1, n + 1)]
        heapify(self.min_heap)

    def reserve(self) -> int:
        return heappop(self.min_heap)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.min_heap, seatNumber)

        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)