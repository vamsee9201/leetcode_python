class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newList = []
        for i,n in enumerate(nums):
            product = 1
            for j,num in enumerate(nums):
                if i != j:
                    product = product*num
            newList.append(product)
        return newList

        