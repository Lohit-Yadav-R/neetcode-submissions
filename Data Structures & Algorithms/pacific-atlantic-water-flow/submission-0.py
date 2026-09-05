class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        atl = [[False] * COLS for _ in range(ROWS)]
        pac = [[False] * COLS for _ in range(ROWS)]
        res = []

        def bfs(beaches, ocean):
            queue = deque(beaches)
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS and 0 <= nc < COLS and
                        not ocean[nr][nc] and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        queue.append((nr, nc))
                        ocean[nr][nc] = True
        
        pacBeaches = []
        atlBeaches = []

        for c in range(COLS):
            pacBeaches.append((0, c))
            pac[0][c] = True
            atlBeaches.append((ROWS - 1, c))
            atl[ROWS - 1][c] = True
        
        for r in range(ROWS):
            pacBeaches.append((r, 0))
            pac[r][0] = True
            atlBeaches.append((r, COLS - 1))
            atl[r][COLS - 1] = True

        bfs(pacBeaches, pac)
        bfs(atlBeaches, atl)

        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])

        return res