class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = 0
        for num in nums:
            if num == 0:
                zero += 1
            if num == 1:
                one += 1
            if num == 2:
                two += 1
        
        nums[:] = [0]*zero + [1]*one + [2]*two
            
        
