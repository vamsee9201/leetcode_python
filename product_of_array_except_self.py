class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zeroes = 0
        product = 1
        for n in nums:
            if n == 0:
                zeroes += 1
            if n != 0:
                product = product*n
        newList = []
        for n in nums:
            if n != 0 and zeroes == 0:
                newNum = product/n
            elif n != 0 and zeroes > 0:
                newNum = 0
            elif n == 0 and zeroes-1 > 0:
                newNum = 0
            elif n == 0 and zeroes -1 == 0:
                newNum = product
            newList.append(newNum)
        return newList
            


        