class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append([r, c])
                    visited.add((r, c))
        
        def addCell(r, c):
            if (
                min(r, c) < 0 or 
                r >= ROWS or 
                c >= COLS or 
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return

            visited.add((r, c))
            queue.append([r, c])
        
        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = 2
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return dist - 1 if dist > 0 else 0