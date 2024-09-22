# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r = 1,n
        badVersion = 0
        while l<=r:
            mid = (l+r)//2
            if isBadVersion(mid):
                r = mid -1
                badVersion = mid
            if not isBadVersion(mid):
                l = mid + 1
        return badVersion





        