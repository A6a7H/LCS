class Solution:
	def countServers(self, grid) -> int:
		def search(row, column):            
			grid[row][column] = 0
			connected = 1
			for nrow in range(row + 1, len(grid)):
				if grid[nrow][column] == 1:
					connected += search(nrow, column)
			for nrow in range(row -1, -1, -1):
				if grid[nrow][column] == 1:
					connected += search(nrow, column)
			for ncolumn in range(column + 1, len(grid[row])):
				if grid[row][ncolumn] == 1:
					connected += search(row, ncolumn)
			for ncolumn in range(column - 1, -1, -1):
			    if grid[row][ncolumn] == 1:
			        connected += search(row, ncolumn)
			return connected
		total = 0
		for row in range(len(grid)):
			for col in range(len(grid[row])):
			    if grid[row][col] == 1:
			        result = search(row, col)
			        total += result if result > 1 else 0
		return total

class Solution:
    def countServers(self, grid) -> int:
        rows = [0 for _ in range(len(grid))]
        cols = [0 for _ in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (cols[j]>1 or rows[i]>1):
                    result += 1
        return result

if __name__ == '__main__':
	s = Solution()
	a = [[1,0,0,1,1],
		[0,0,0,0,0],
		[0,0,0,1,0]]
	print([0 for _ in range(len(a))])	
	print(s.countServers(a))