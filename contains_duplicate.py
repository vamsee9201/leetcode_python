class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numMap = {}
        for n in nums:
            numMap[n] = 1+numMap.get(n,0)
        
        for v in numMap.values():
            if v > 1:
                return True
        return False
        