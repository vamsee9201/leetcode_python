class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = []
        one = []
        two = []
        for num in nums:
            if num == 0:
                zero.append(num)
        print(zero)
        for num in nums:
            if num == 1:
                one.append(num)
        for num in nums:
            if num == 2:
                two.append(num)
        nums[:] = zero+one+two
        
