class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted((carPos, carNum) for carNum, carPos in enumerate(position))
        stack = []
        for car in range(len(cars)):
            carPos = cars[car][0]
            carSpeed = speed[cars[car][1]]
            time = (target - carPos) / carSpeed
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        
        return len(stack)