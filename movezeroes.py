class Solution(object):
  def moveZeroes(self,nums):
    j=0
    for i in range(len(nums)):
      if nums[i]!=0:
        nums[j],nums[i]=nums[i],nums[j]
        j+=1
    return nums

Time complexity O(n)
pace Complexity  O(1)
