class Solution(object):
  def maximumSubarraySum(self, nums, k):
    max_sum = 0
    current_sum = 0
    freq = {}
    for i, num in enumerate(nums):
      current_sum += num
      freq[num] = freq.get(num, 0) + 1
      if i >= k:
        left = nums[i - k]
        current_sum -= left
        freq[left] -= 1
        if freq[left] == 0:
          del freq[left]
      if i >= k - 1 and len(freq) == k:
        if current_sum > max_sum:
          max_sum = current_sum
    return max_sum