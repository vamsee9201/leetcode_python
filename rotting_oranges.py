class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows,cols = len(grid),len(grid[0])
        visit = set()
        sq = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 and (r,c) not in visit:
                    sq.append((r,c))
                    visit.add((r,c))
        minutes = 0
        print(sq)
        while sq:
            row,col = sq.popleft()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                r,c = row + dr,col + dc
                if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visit:
                    sq.append((r,c))
                    visit.add((r,c))
            print(sq)
            minutes += 1
            print(minutes)
        return minutes


        

        

        

                
        