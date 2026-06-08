class Solution(object):
  def maxSubarray(self,nums):
    current_sum=nums[0]
    best_sum=nums[0]
    for num in nums[1:]:
      current_sum+=num
      if current_sum<num:
        current_sum=num
      if current_sum>best_sum:
        best_sum=current_sum
    return best_sum

Time complexity: O(n)
