class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows,cols = len(grid),len(grid[0])


        q = collections.deque()
        visit = set()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 and (r,c) not in visit:
                    q.append((r,c))
                    visit.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        minutes = 0
        while q and fresh > 0:
            for i in range(len(q)):
                row,col = q.popleft()
                for dr,dc in directions:
                    r,c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))
                        fresh -= 1
            minutes += 1
        return minutes if fresh == 0 else -1

        