#Problem Two_sum
#platform Leetcode

def two_sum(self,nums,target):
  hashmap={}
  for i,num in enumerate(nums):
    diff=target-num
    if diff in hashmap:
      return(hashmap[diff],i)
    hashmap[num]=i
