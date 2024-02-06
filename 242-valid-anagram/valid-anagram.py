class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        num_s, num_t = {}, {}

        for i in range(len(s)):
            num_s[s[i]] = num_s.get(s[i], 0) + 1
            num_t[t[i]] = num_t.get(t[i], 0) + 1

        for j in num_s:
            if num_s[j] != num_t.get(j, 0):
                return False
        
        return True