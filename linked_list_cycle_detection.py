# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        listOfNodes = []
        curr = head
        while curr:
            if curr in listOfNodes:
                return True
            listOfNodes.append(curr)
            curr = curr.next

            


        