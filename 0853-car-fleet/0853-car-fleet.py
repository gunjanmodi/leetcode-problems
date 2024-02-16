class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = list(zip(position, speed))
        cars.sort(key= lambda x:x[0])
        time_to_reach = [(target-car[0]) / car[1] for car in cars]

        fleets = 0
        current_max_time = float('-inf')
        for i in reversed(range(n)):
            if time_to_reach[i] > current_max_time:
                current_max_time = time_to_reach[i]
                fleets += 1
        return fleets