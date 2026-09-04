class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(position[i], speed[i]) for i in range(len(position))], reverse=True)
        fleets = 0
        slowtime = 0.0
        
        for carpos, carspeed in cars:
            time = (target - carpos) / carspeed
            if time > slowtime:
                fleets += 1
                slowtime = time
                
        return fleets