class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def doDfs(row, col):
            self.count += 1
            grid[row][col] = 0
            if (row + 1 < len(grid) and grid[row+1][col] == 1):
                doDfs(row+1, col)
            if (row - 1 >= 0 and grid[row-1][col] == 1):
                doDfs(row-1, col)
            if (col - 1 >= 0 and grid[row][col-1] == 1):
                doDfs(row, col-1)
            if (col + 1 < len(grid[row]) and grid[row][col+1] == 1):
                doDfs(row, col+1)
                
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == 1):
                    self.count = 0;
                    doDfs(i, j);
                    if(self.count > ans):
                        ans = self.count;
        return ans