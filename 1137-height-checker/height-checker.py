class Solution(object):
    def heightChecker(self, heights):
        n=len(heights)
        count=0
        h=sorted(heights)
        for i in range(n):
            if heights[i]!=h[i]:
                count+=1
        return count
        