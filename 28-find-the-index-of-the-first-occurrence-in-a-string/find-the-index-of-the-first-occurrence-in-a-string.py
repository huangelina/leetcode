class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_haystack = len(haystack)
        len_needle = len(needle)

        for char in range(len_haystack - len_needle + 1):
            if haystack[char:char + len_needle] == needle:
                return char
        
        return -1
