from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start = None
        litters = []
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litters.append((r, c))

        num_litters = len(litters)
        litter_map = {pos: i for i, pos in enumerate(litters)}
        target_mask = (1 << num_litters) - 1

        sr, sc = start
        
        initial_mask = 0
        if (sr, sc) in litter_map:
            initial_mask |= (1 << litter_map[(sr, sc)])
            
        if initial_mask == target_mask:
            return 0

        # State: (r, c, energy, mask)
        queue = deque([(sr, sc, energy, initial_mask, 0)])
        visited = set([(sr, sc, energy, initial_mask)])

        while queue:
            r, c, e, mask, moves = queue.popleft()

            if e == 0:
                continue

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    cell = classroom[nr][nc]
                    
                    ne = energy if cell == 'R' else e - 1
                    nmask = mask
                    
                    if cell == 'L':
                        nmask |= (1 << litter_map[(nr, nc)])
                        
                    if nmask == target_mask:
                        return moves + 1

                    state = (nr, nc, ne, nmask)
                    if state not in visited:
                        visited.add(state)
                        queue.append((nr, nc, ne, nmask, moves + 1))

        return -1