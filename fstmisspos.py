class Solution:
    def firstMissingPositive(self, nums):
        """
        Given an unsorted integer array, find the smallest missing positive integer.
        Your algorithm should run in O(n) time and uses O(1) extra space.

        :type nums: List[int]
        :rtype: int
        """
        # [44 ms]
        # method 1
        # early break
        if 1 not in nums: return 1
        if len(nums)==1: return 2

        # for any k positive numbers (duplicates allowed), 
        # the first missing positive number must be within [1,k+1]
        
        # since there can be some non-postive integers
        # need to partition the array and put positive numbers on one side
        # partition function is like quick sort partition(not the same), this is O(n) time, O(1) space
        
        def partition(nums):
            ''' patition the nums array in place,
                return the pivot, which is k=number of positive integers in the nums'''
            pivot=0
            for i in range(len(nums)):
                if nums[i]>0:
                    # move the positive number to the left of the pivot
                    temp=nums[pivot]
                    nums[pivot]=nums[i]
                    nums[i]=temp

                    pivot+=1

            return pivot

        k = partition(nums)
        fstmidx = k

        # now the first k elements in the nums are all positive
        # then using the nums[i] to indicate whether there exists the integer=i-1
        # besides, if the integer=i-1 is larger than k, we can pass it
        # if exists, then set the nums[i] to negetive
        for i in range(k):
            temp = abs(nums[i])
            if temp<=k:
                # the integer valued temp do exist, then set the nums[temp-1] to negetive
                if nums[temp-1] > 0:
                    nums[temp-1] *= -1

        # finally scan the first k elements
        # and find out the first missing positive = first missing idx + 1
        for i in range(k):
            if nums[i]>0:
                fstmidx=i
                break

        return fstmidx+1
        
        # [44 ms]
        # method 2
        n = len(nums)
        if 1 not in nums:
            return 1
        if n == 1:
            return 2
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                # since there must exist number 1 in the array, otherwise would return 1 in line 65
                nums[i] = 1
        for i in range(n):
            temp = abs(nums[i])
            if nums[temp-1]>0:
                nums[temp-1] *= -1
        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1



sol=Solution()
numslis=[[0,1,2,4],[-1,1,2,3],[6,7,9,4]]
for nums in numslis:
    numscopy = nums.copy()
    print("The smallest positive integer in the nums=%s is: %d" %(numscopy, sol.firstMissingPositive(nums)))
