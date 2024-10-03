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
        #newList = []
        for j,n in enumerate(nums):
            if n != 0 and zeroes == 0:
                nums[j] = product/n
            elif n != 0 and zeroes > 0:
                nums[j] = 0
            elif n == 0 and zeroes-1 > 0:
                nums[j] = 0
            elif n == 0 and zeroes -1 == 0:
                nums[j] = product
            #newList.append(newNum)
        return nums
            


        