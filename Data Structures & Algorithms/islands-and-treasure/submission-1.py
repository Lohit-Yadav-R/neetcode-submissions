class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        queue = deque()
 
        for r in range((ROWS)):
            for c in range((COLS)):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))

        def addCell(r, c):
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == -1 or (r, c) in visited):
                return

            visited.add((r, c))
            queue.append([r, c])
        
        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1