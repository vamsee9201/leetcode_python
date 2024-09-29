class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        queue = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ans = [[0]*n for _ in range(m)]
        visited = set()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                i,j = queue.popleft()
                if mat[i][j] == 1:
                    ans[i][j] = dist

                for d in directions:
                    ni = i + d[0]
                    nj = j + d[1]

                    if 0 <= ni < m and 0 <= nj < n and (ni,nj) not in visited:
                        queue.append((ni,nj))
                        visited.add((ni,nj))


            dist += 1
        return ans 
