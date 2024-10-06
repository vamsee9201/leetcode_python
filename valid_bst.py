# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(root):
           
            if not root:
                return [True,None,None,None]
            print(root.val)

            left,right = dfs(root.left),dfs(root.right)
            if not left[1] or root.val > left[1]:
                leftOk = True
            else:
                leftOk = False

            if not right[1] or root.val < right[1]:
                rightOk = True
            else:
                rightOk = False
            
            if not left[2] or left[2] > left[1]:
                leftOk = True
                leftmin = left[1]
            else:
                leftOk = False
                leftmin = left[1]
            
            if not right[3] or right[3] < right[1]:
                rightOk = True
                rightMax = right[1]
            else:
                rightOK = False
                rightMax = right[1]

            isValid = (leftOk and rightOk) and (left[0] and right[0])
            return (isValid,root.val,leftmin,rightMax)
        return dfs(root)[0]
        #return True


            
                
        