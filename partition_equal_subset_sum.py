class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2 :
            return False

        dp = set()
        dp.add(0)
        target = sum(nums)//2

        for i in range(len(nums) -1,-1,-1):
            nextDp = set()
            for t in dp:
                nextDp.add(nums[i] + t)
                nextDp.add(t)
            dp = nextDp
        return True if target in dp else False
