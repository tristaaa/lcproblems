class Solution:
    def containsNearbyDuplicate(self, nums, k, t):
        """
        Given an array of integers, an integer k and an integer t, 
        find out whether there are two distinct indices i and j in the array such that 
        the absolute difference between nums[i] and nums[j] is at most t 
        and the absolute difference between i and j is at most k.


        type nums: List[int]
        type k: int
        type t: int
        rtype: bool 
        """

        # Hint: 
        # 1). using balanced tree 
        # - Time complexity O(nlogk), This will give an indication that sorting is involved for k elements.
        # - Use already existing state to evaluate next state,
        #     Like, a set of k sorted numbers are only needed to be tracked. 
        #     When we are processing the next number in array, 
        #     then we can utilize the existing sorted state 
        #     and it is not necessary to sort next overlapping set of k numbers again.
        
        # 2). using bucket O(n)
        # there's a constraint on the range of the values of the elements to be considered duplicates,
        # it reminds us of doing a range check which is implemented in tree data structure and O(LogN) 
        # if using a balanced tree structure is used, or doing a bucket check which is constant time.
        # [60 ms]
        if k<0 or t<0: return False

        seen={}
        # using a size of t+1(since can be zero) to make sure 
        # the duplicates are in same bucket or adjacent bucket
        bucketsize = t+1
        # always keep track of the subset numbers of size k+1, nums[i-k:i+1]
        for i in range(len(nums)):
            bucketidx = nums[i]//bucketsize
            if bucketidx in seen \
                or (bucketidx-1) in seen and abs(nums[i]-seen[bucketidx-1])<=t \
                or (bucketidx+1) in seen and abs(nums[i]-seen[bucketidx+1])<=t:
                return True

            seen[bucketidx] = nums[i]
            if len(seen)>k:
                del seen[nums[i-k]//bucketsize]

        return False

sol=Solution()
nums = [1,5,9,1,5,9]
k = 2
t = 3
print("Given the array: %s, there are two idx i and j such that the absolute difference between nums[i] and nums[j] are <=t (t=%d) and the absolute difference between i and j are <=k (k=%d): %s" % (nums,t,k,sol.containsNearbyDuplicate(nums,k,t)))

            
