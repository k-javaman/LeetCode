class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # don't have to filled because of [0]
        res = [0] * len(temperatures) # create a list of 0s with the same length as the input list
        stack = [] # create an empty stack to store pairs of temperature and index
        
        for i, t in enumerate(temperatures): # loop through each temperature in the input list
            while stack and t > stack[-1][0]: # while the stack is not empty and the current temperature is greater than the temperature at the top of the stack
                stackT, stackInd = stack.pop() # pop the top element from the stack and store its temperature and index
                res[stackInd] = (i - stackInd) # calculate the difference between the current index and the popped index and store it in the result array at the popped index
            stack.append([t, i]) # add the current temperature and index to the stack
        
        return res # return the result array
    
    # The function uses a stack to keep track of the indices of temperatures that are lower than the current temperature. The stack stores pairs of temperature and index. For each temperature in the input list, we check if it is greater than the temperature at the top of the stack. If it is, we pop the top element from the stack and calculate the difference between its index and the current index. We then store this difference in the result array at the popped element’s index.
# The time complexity of this function is O(n), where n is the length of the input list.
                        