class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matches = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for char in s:
            if char in matches:
                if stack and stack[-1] == matches[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if not stack:
            return True
        else:
            return False
