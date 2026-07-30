class Solution:
    def largestInteger(self, n, s):
        if s > 9 * n:
            return -1
        if s == 0:
            return 0
        ans = ""
        while n:
            digit = min(9,s)
            ans += str(digit)
            s -= digit
            n -= 1
        return int(ans)


        