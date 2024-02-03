class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        last_digit = len(digits)
        n = last_digit - 1
        while n >= 0:
            if digits[n] == 9:
                digits[n] = 0
                n -= 1
            else:
                digits[n] += 1
                return digits

        result = [0] * (last_digit + 1)
        result[0] = 1
        return result

