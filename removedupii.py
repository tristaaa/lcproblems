class Solution:
    def removeDuplicates(self, nums):
        '''
        Given a sorted array nums, 
        remove the duplicates in-place such that 
        duplicates appeared at most twice and return the new length.
        '''
        # [92 ms]
#         initialize a pointer for a distinct element
        cnt=1
        for i in range(2,len(nums)):
#             skip the duplicate if it appears more than twice
            if nums[cnt]==nums[i] and nums[cnt-1]==nums[i]:
                continue
            else:
                cnt+=1
            nums[cnt]=nums[i]
        return cnt+1

sol = Solution()
# nums=[0,1,1,1,1,1,2,3,3]
nums=[0,0,0,1,1,1,1,2,3,3]
nums_origin = nums.copy()
newlen=sol.removeDuplicates(nums)
print("the length of the `nums`=%s after removing the duplicates is: %d, which becomes: %s" %(nums_origin,newlen,nums[:newlen]))
