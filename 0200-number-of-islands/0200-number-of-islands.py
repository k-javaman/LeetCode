# Class definition for the solution
class Solution:

    # Function to find the number of islands in the grid
    def numIslands(self, grid: List[List[str]]) -> int:

        # If grid is empty, return 0
        if not grid: return 0

        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])

        # Initialize the island count to 0
        ans = 0

        # Loop through each cell in the grid
        for i in range(m):
            for j in range(n):

                # If the cell is part of an island (value is '1')
                if grid[i][j] == '1':

                    # Create a queue for BFS and add the current cell to it
                    grid[i][j] = '2'
                    q = collections.deque([(i, j)])

                    # Mark the current cell as visited by changing its value to '2'
                    

                    # While there are still cells to visit in the queue
                    while q:

                        # Dequeue a cell for exploration
                        x, y = q.popleft()

                        # Check the four adjacent cells (right, left, below, above)
                        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):

                            # Compute the coordinates of the adjacent cell
                            xx, yy = x+dx, y+dy

                            # If the adjacent cell is within the grid boundaries and is part of an island
                            if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == '1':

                                # Add the adjacent cell to the queue for future exploration
                                q.append((xx, yy))

                                # Mark the adjacent cell as visited
                                grid[xx][yy] = '2'

                    # After exploring all cells of the current island, increment the island count
                    ans += 1

        # Return the total number of islands
        return ans
