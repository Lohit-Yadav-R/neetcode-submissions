class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        exposed = set()

        def bfs(edgeCells):
            queue = deque(edgeCells)
            for cell in edgeCells:
                exposed.add(cell)

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS and 0 <= nc < COLS and
                        (nr, nc) not in exposed and
                        board[nr][nc] == 'O'
                    ):
                        queue.append((nr, nc))
                        exposed.add((nr, nc))
        
        edgeCells = []
        for r in range(ROWS):
            if board[r][0] == 'O':
                edgeCells.append((r, 0))
            if board[r][COLS - 1] == 'O':
                edgeCells.append((r, COLS - 1))
        for c in range(COLS):
            if board[0][c] == 'O':
                edgeCells.append((0, c))
            if board[ROWS - 1][c] == 'O':
                edgeCells.append((ROWS - 1, c))
        
        bfs(edgeCells)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in exposed and board[r][c] == 'O':
                    board[r][c] = 'X'