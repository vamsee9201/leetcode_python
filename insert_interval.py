class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        newIntervals = []
        def isOverlap(interval1,interval2):
            if (interval1[0] >= interval2[0] and interval1[0] <= interval2[1]) or (interval1[1] >= interval2[0] and interval1[1] <= interval2[1]) :
                return True
            else:
                return False
        added = False
        active = False
        for interval in intervals:
            #checking overlap with new interval
            if isOverlap(interval,newInterval):
                print(True)
                firstElement = min(interval[0],newInterval[0])
                print(firstElement)
                secondElement = max(interval[1],newInterval[1])
                print(secondElement)
                newInterval = [firstElement,secondElement]
            else:
                newIntervals.append(interval)
        newIntervals.append(newInterval)
        return newIntervals
            

        