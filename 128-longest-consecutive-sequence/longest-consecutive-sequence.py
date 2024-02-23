class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ordered_nums = set(nums)
        longest = 0

        for num in ordered_nums:
            if (num - 1) not in ordered_nums:
                length = 1
                while (num + length) in ordered_nums:
                    length += 1
                longest = max(length, longest)
        return longest