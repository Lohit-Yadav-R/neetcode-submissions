class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def mapIsland(area, r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
                return area + 0
            grid[r][c] = 0
            for dr, dc in directions:
                area = mapIsland(area, r + dr, c + dc)
            return area + 1
            
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    area = mapIsland(0, r, c)
                    res = max(res, area)
        
        return res
