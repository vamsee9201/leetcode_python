# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # rootLength = 0
        # increment = 1
        # length = 7
        # while rootLength != 7:
        #     rootLength = rootLength + increment
        #     increment = increment*2
        #     print(rootLength)

        if not root:
            return None
        
        temp=root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        



