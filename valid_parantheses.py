class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pMap = {"}":"{","]":"[",")":"("}
        for p in s:
            if p in pMap:
                if stack and stack[-1] == pMap[p]:
                    stack.pop()
                else :
                    return False
            else :
                stack.append(p)
        if not stack:
            return True
        