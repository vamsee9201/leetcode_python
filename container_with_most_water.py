class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1

        area = -1
        while l < r:
            b = min(height[l],height[r])
            length = r - l
            currentArea = length*b
            if currentArea > area:
                area = currentArea

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area
            

        