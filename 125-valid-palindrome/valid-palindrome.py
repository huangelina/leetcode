class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        word = ''.join([c for c in s.lower() if c.isalnum()])
        temp = len(word)
        result = True
        for char in range(temp):
            if word[char] != word[temp - 1 - char]:
                result = False
        return result
        