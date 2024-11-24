class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s) :
            return []
        
        sCount,pCount = {},{}

        for i in range(len(p)):
            pCount[p[i]] = pCount.get(p[i],0) + 1
            sCount[s[i]] = sCount.get(s[i],0) + 1
        
        res = [0] if pCount == sCount else []
        l = 0
        for i in range(len(p),len(s)):
            sCount[s[i]] = sCount.get(s[i],0) + 1
            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                res.append(l)
        return res
