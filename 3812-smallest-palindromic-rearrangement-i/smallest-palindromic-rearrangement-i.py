class Solution(object):
    def smallestPalindrome(self, s):
        n=len(s)
        if n==1:
            return s
        half=list(s[:n//2])
        half.sort()
        if n%2==0:
            return ''.join(half) + ''.join(half[::-1])
        x=s[n/2]
        return ''.join(half) + x+''.join(half[::-1])
        