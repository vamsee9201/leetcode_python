class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        print(ord("0"))
        print(ord("9"))
        check = ""
        for i in range(len(s)):
            if (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122) or  (ord(s[i]) >= 48 and ord(s[i]) <= 57):
                check = check + s[i]
        check = lower(check)
        print(check)
        if check == check[-1::-1]:
            return True
        else:
            return False
                

        