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
        lowestOccuringEvenCharacter = 2001
        for key,value in stringMap.items():
            if (not odd) and (value%2 != 0):
                odd = True
                palindromeLength += value
            elif odd and (value%2 != 0):
                palindromeLength += value-1
            else:
                pass
            if value%2 == 0:
                palindromeLength += value
                if value < lowestOccuringEvenCharacter:
                    lowestOccuringEvenCharacter = value

        # if palindromeLength%2 == 0:
        #     palindromeLength = palindromeLength - (lowestOccuringEvenCharacter - 1)
        print(stringMap)
        return palindromeLength

        
        

        
        