class Solution(object):
  def merge(self,nums1,m,nums2,n):
    while len(nums1)>m:
      nums1.pop()
    for i in range(n):
      nums1.append(nums2[i])
    nums1.sort()

Time complexity O((m+n)log(m+n))
Space complexity O(1)
