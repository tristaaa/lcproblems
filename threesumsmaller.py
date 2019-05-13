class Solution:
    def threeSumSmaller(self, nums, target):
        """
            Find the number of index triplets (i,j,k) with 0<=i<j<k<n 
            that satisfy the condition: nums[i]+nums[j]+nums[k] < target.

            :type nums: List[int]
            :type target: int
            :rtype: int
        """
        # using two pointers
        nums.sort()
        count = 0
        if len(nums)<3: return count
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]<target:
                    # the third number: nums[r] could be any number that between nums[l] & nums[r]
                    count+= r-l 
                    l+=1
                else:
                    r-=1
        return count





# test
nums = [-2,0,1,3]
target = 2
sol = Solution()
print("number of index triplets whose summation is smaller than target(%d) is: %d" % (target, sol.threeSumSmaller(nums,target)))