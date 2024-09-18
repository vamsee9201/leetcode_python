class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r = 0,len(s)-1
        while l < r:
            while l <r and not self.isAlphaNum(s[l]):
                l +=1
            while r>l and not self.isAlphaNum(s[r]):
                r -=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
    def isAlphaNum(self,c):
        return( (ord(c) >= 65 and ord(c) <= 90) or 
        (ord(c) >= 97 and ord(c) <= 122) or  
        (ord(c) >= 48  and ord(c) <= 57))

        