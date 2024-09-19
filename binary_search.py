class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start<=end:
            print(start)
            print(end)
            mid = (start+end)/2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                start = mid+1
            if target < nums[mid]:
                end = mid -1
        return -1


        