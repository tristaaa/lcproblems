class Solution:
    def removeElement(self, nums, val):
        """Given an array nums and a value val, 
            remove all instances of that value in-place 
            and return the new length."""
        cnt=0
        i=0
        length=len(nums)
        while i<length:
            if nums[i]==val:
                cnt+=1
            else:
                nums[i-cnt]=nums[i]
            i+=1
        return i-cnt

sol = Solution()
nums=[0,1,2,2,3,0,4,2]
val=2
print("the length of the `nums`=%s after removing the value=%d is: %d" %(nums,val,sol.removeElement(nums, val)))
