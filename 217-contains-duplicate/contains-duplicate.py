class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ordered = set()
        for num in nums:
            if num in ordered:
                return True
            ordered.add(num)
        return False
        