# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        total = 0
        while curr:
            total +=1
            curr = curr.next
        
        target = total//2 + 1
        curr = head
        for i in range(1,total+1):
            if i == target:
                return curr
            curr = curr.next
            

        