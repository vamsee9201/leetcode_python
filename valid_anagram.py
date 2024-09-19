class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #hashmap solution
        if len(s) != len(t):
            return False
        countS,countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0) + 1
            countT[t[i]] = countT.get(t[i],0) + 1
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True
        