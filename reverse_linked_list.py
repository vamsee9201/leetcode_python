# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # curr = head
        # listNodes = []
        # while curr:
        #     listNodes.append(ListNode(curr.val))
        #     curr = curr.next
        # dummy = ListNode(0)
        # returndummy = dummy
        # for node in listNodes[-1::-1]:
        #     dummy.next = node
        #     dummy = dummy.next
        # return returndummy.next
        curr,prev = head,None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

            


            