# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        mergedList = ListNode(0,None)
        curr = mergedList
        curr1 = list1
        curr2 = list2
        while (curr1 is not None) and (curr2 is not None):
            while curr1 and curr2 and curr1.val <= curr2.val:
                curr.next = ListNode(curr1.val,None)
                curr = curr.next
                curr1 = curr1.next
            while curr1 and curr2 and curr2.val <= curr1.val:
                curr.next = ListNode(curr2.val,None)
                curr = curr.next
                curr2 = curr2.next
        if curr1:
            curr.next = curr1
        if curr2:
            curr.next = curr2
        return mergedList.next 


                
        