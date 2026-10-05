class Solution:
    def reverseDegree(self, s):
        total=0
        for indx,val in enumerate(s):
            reverse_val=26-(ord(val)-ord("a"))
            position=indx+1
            total+=reverse_val*position
        return total
        