class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pMap = {"}":"{","]":"[",")":"("}
        for p in s:
            if p == "(" or p == "[" or p == "{":
                stack.append(p)
            if p == ")" or p == "]" or p == "}":
                if stack and stack[-1] == pMap[p]:
                    stack.pop()
                else :
                    return False
        if not stack:
            return True
        