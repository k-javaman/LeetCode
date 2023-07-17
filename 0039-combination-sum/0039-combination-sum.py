# Class definition, following Python's Object-Oriented Programming (OOP) conventions
class Solution:
    # combinationSum method declaration which takes an array of integers (candidates) and a target integer as parameters
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize an empty list to hold all the combinations that add up to the target
        res = []

        # Define a helper function dfs that performs Depth-First Search. It takes an index 'i', a list 'cur' and a sum 'total'
        def dfs(cur, i, total):
            # If total equals the target, it means we found a valid combination, so append it to 'res'
            if total == target:
                res.append(cur.copy())
                return
            # If the index 'i' is out of range, or if total is greater than the target, we stop searching along this path
            if i >= len(candidates) or total > target:
                return

            # We add the current candidate to the list 'cur' and the sum 'total'
            cur.append(candidates[i])
            # Call the dfs function recursively, keeping the same index 'i'. This allows us to reuse the same number
            dfs(cur, i, total + candidates[i])
            # We remove the last added candidate. This is known as backtracking, and is necessary to search for all possible combinations
            cur.pop()
            # Call the dfs function recursively, but incrementing the index 'i' to move on to the next candidate
            dfs(cur, i+1, total)

        # We kick off the Depth-First Search with the initial call of dfs function
        dfs([], 0, 0)
        # We return the list of all combinations that add up to the target
        return res
