class Solution(object):
    def countOdds(self, low, high):
        return (high+(high&1)-low+(low&1))>>1