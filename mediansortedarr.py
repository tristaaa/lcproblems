class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        """
            nums1 and nums2 are two sorted array of size m and n, 
            return the median of the the two sorted arrays, runtime complexity must be O(log(m+n))

            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: float
        """
        # [116 ms]
        # Find the kth number of the merged array `sorted(nums1+nums2)`, 
        # Divide&Conquer, recursively find the median number of two sorted arr
        # Since the left half of the array with a smaller submedian can never contains the common median, drop it
        # the subproblem is reduce to find the median of two sorted array with one array being cut half
        # Notice that here the k is the idx 
        def findKidx(nums1,nums2,l1,l2,r1,r2,k):
            print(k,l1,l2,r1,r2)
            if l1 > r1: return nums2[l2+k]
            if l2 > r2: return nums1[l1+k]

            if k==0: return min(nums1[l1+k],nums2[l2+k])

            idx1,idx2 = (l1+r1)//2,(l2+r2)//2
            mid1,mid2 = nums1[idx1],nums2[idx2]

            # now we respectively spilt the two array into two parts, by the mid idx
            # since the arr are sorted, by comparing the two mid elements 
            # we can know which part is largest and which is smallest
            # if the kth idx is larger then we can drop the smallest part, since the number in idx k won't be in this part
            # else we can drop the largest part 
            if idx1+idx2-l1-l2<k:
                if mid1<mid2:
                    # the number of elements we droped is idx1-l1+1, 
                    # so the k need to be adjusted to k-(idx1-l1+1)
                    return findKidx(nums1,nums2,idx1+1,l2,r1,r2,k-idx1+l1-1)
                else:
                    return findKidx(nums1,nums2,l1,idx2+1,r1,r2,k-idx2+l2-1)
            else:
                if mid1<mid2:
                    return findKidx(nums1,nums2,l1,l2,r1,idx2-1,k)
                else:
                    return findKidx(nums1,nums2,l1,l2,idx1-1,r2,k)


        m,n=len(nums1),len(nums2)
        # if the length of the merged array is odd
        if (m+n)&1: 
            return findKidx(nums1,nums2,0,0,m-1,n-1,(m+n)//2)*1.0
        else:
            return (findKidx(nums1,nums2,0,0,m-1,n-1,(m+n)//2)+findKidx(nums1,nums2,0,0,m-1,n-1,(m+n)//2-1)) / 2


sol = Solution()
nums1,nums2=[1,2],[3,4]
result=sol.findMedianSortedArrays(nums1,nums2)
print("the median of the two sorted array: %s, %s is: %s" % (nums1,nums2,result))
