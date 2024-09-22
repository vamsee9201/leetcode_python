class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomMap = {}
        magazineMap = {}
        for i in range(len(ransomNote)):
            ransomMap[ransomNote[i]] = ransomMap.get(ransomNote[i],0) + 1
        for i in range(len(magazine)):
            magazineMap[magazine[i]] = magazineMap.get(magazine[i],0) + 1
        print(ransomMap)
        print(magazineMap)
        for c in ransomMap:
            if magazineMap.get(c,0) < ransomMap[c]:
                return False
        return True

            

        