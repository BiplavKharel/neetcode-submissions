class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        car_info = list(zip(position,speed))
        car_info.sort(key = lambda x:x[0])
        print(car_info)
        time_to_reach = [(target - x[0])/x[1] for x in car_info]
        
        num_fleets = 1
        prev_time = time_to_reach[len(car_info) - 1]
        print(time_to_reach)
        while time_to_reach:
            time = time_to_reach[-1]
            if time > prev_time:
                num_fleets +=1
                prev_time = time
            time_to_reach.pop()
            

        return num_fleets

        