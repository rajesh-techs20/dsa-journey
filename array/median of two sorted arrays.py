#median of two sorted arrays
#leetcode

def findMedianSortedArrays(self, nums1, nums2):
        nums=nums1+nums2
        nums.sort()
        n=len(nums)
        if n%2==0:
            med =(nums[n//2-1]+nums[n//2])/2.0
        else:
            med=nums[n//2]
        return med


        
