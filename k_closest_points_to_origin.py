import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def calculateDistance(point):
            dist = sqrt(point[0]**2 + point[1]**2)
            return dist
        
        heap = [ (calculateDistance(point),point) for point in points]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]


            
        