class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals or len(intervals) == 1:
            return intervals
        curInterval = intervals[0]
        def isOverlap(i1,i2):
            overlap = False
            if (i2[0] <= i1[1] and i2[0] >= i1[0]) or (i2[1] <= i1[1] and i2[1] >= i1[0]) or (i1[0] <= i2[1] and i1[0] >= i2[0]) or (i1[1] <= i2[1] and i1[1] >= i2[0]) :
                overlap = True
            return overlap
        res = []
        curInterval = []
        intervals = sorted(intervals)
        for interval in intervals:
            if not curInterval:
                curInterval = interval
                continue
            
            print(interval)
            print(curInterval)
            print(isOverlap(interval,curInterval))
            if isOverlap(interval,curInterval):
                first = min(interval[0],curInterval[0])
                second = max(interval[1],curInterval[1])
                curInterval = [first,second]
            else:
                res.append(curInterval)
                curInterval = interval
        res.append(curInterval)
        return res

            
        

        #print(ifOverlap([4,5],[1,4]))
        