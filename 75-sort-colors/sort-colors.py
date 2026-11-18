class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        swapped = True
        while swapped:
            swapped = False
            for i in range(0, n - 1):
                current_element = nums[i]
                next_element = nums[i + 1]
                if current_element > next_element:
                    temp = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = temp
                    swapped = True