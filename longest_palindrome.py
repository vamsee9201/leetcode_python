class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        stringMap = {}
        for c in s:
            stringMap[c] = stringMap.get(c,0) + 1
        
        odd = False
        palindromeLength = 0
        for key,value in stringMap.items():
            if value%2:
                palindromeLength += value-1
                odd = True
            if value%2 == 0:
                palindromeLength += value


        if odd:
            return (palindromeLength + 1)
        return palindromeLength

        
        

        
        