class Solution(object):
    def romanToInt(self, s):
        result = 0
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}

        for a, b in zip(s, s[1:]):
            if roman_dict[a] < roman_dict[b]:
                result -= roman_dict[a]
            else:
                result += roman_dict[a]
        return result + roman_dict[s[-1]]
        