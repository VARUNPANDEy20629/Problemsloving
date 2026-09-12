class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = [-1] * n
        st = []
        for i in range(2* n -1, -1, -1):
            num = nums[i % n]
            while st and st[-1] <= num:
                st.pop()
            if i < n and st:
                ans[i] = st[-1]
            st.append(num)
        return ans