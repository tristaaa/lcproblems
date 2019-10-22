class Solution:
    def containsDuplicate(self, nums):
        """
        Given an array of integers, find if the array contains any duplicates.
        return true if any value appears at least twice

        type nums: List[int]
        rtype: bool
        """
        seen=set()
        flag=False
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                flag=True
        return flag

sol = Solution()
nums=[1,2,3,1]
print("the given array: %s contains duplicate numbers: %s" % (nums,sol.containsDuplicate(nums)))
