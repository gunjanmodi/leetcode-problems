class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        seating = [0 for _ in range(1001)]
        
        for passengers, from_point, to_point in trips:
            seating[from_point] += passengers
            seating[to_point] -= passengers

        current = 0
        for i in range(1001):
            current += seating[i]
            if current > capacity:
                return False
        return True
