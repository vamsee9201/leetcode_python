class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0

        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                newLen = r - l + 1
                if newLen > resLen:
                    resLen = newLen
                    res = s[l:r+1]
                l -= 1
                r += 1

            l,r = i,i+1
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                newLen = r - l + 1
                if newLen > resLen:
                    resLen = newLen
                    res = s[l:r+1]
                l -= 1
                r += 1


        return res
