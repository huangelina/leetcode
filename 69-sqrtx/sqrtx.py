class Solution(object):
    def mySqrt(self, x):
        search = x
        while not search * search - x < 1:
            search = (search + x / search) / 2
        return int(search)
        