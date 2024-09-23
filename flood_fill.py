class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        current_color = image[sr][sc]
        height = len(image)
        width = len(image[0])
        def dfs(sr,sc):
            if 0 <= sr < height and 0 <= sc < width and image[sr][sc] == current_color and image[sr][sc] != color:
                image[sr][sc] = color
                dfs(sr+1,sc)
                dfs(sr-1,sc)
                dfs(sr,sc+1)
                dfs(sr,sc-1)
        dfs(sr,sc)
        return image
        
        