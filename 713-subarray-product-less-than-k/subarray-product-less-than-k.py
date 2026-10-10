class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        ans = 0
        product = 1
        left = 0
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k and left <= right:
                product //= nums[left]
                left += 1
            ans += (right - left + 1) 
        return ans