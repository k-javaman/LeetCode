class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = prev = 0 # Initialize ans and prev to 0
        for pp, ss in sorted(zip(position, speed), reverse=True): # Sort the position and speed arrays in descending order of position
            tt = (target - pp)/ss # Calculate the time it takes for the car to reach the target
            if  prev < tt: # If the time it takes to reach the target is greater than the previous car's time
                ans += 1 # Increment the number of car fleets
                prev = tt # Update the previous car's time
        return ans # Return the number of car fleets