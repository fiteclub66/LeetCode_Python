class Solution(object):
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return 0
        grid[i][j] = "0"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island_count = 0
        if len(grid) <= 0:
            return 0

        for i in range (len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j] == "1":
                    island_count += 1
                    self.dfs(grid, i, j)
        return island_count