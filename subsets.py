class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subset = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j > i:
                    toAdd = [nums[i],nums[j]]
                    subset.append(toAdd)
        for n in nums:
            subset.append([n])
        subset.append([])
        if nums not in subset :
            subset.append(nums)
        else:
            pass
        return subset
