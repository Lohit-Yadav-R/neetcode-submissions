class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def mapIsland(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0'):
                return
            grid[r][c] = '0'
            for dr, dc in directions:
                mapIsland(r + dr, c + dc)
            
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    mapIsland(r, c)
                    res += 1
        
        return res
