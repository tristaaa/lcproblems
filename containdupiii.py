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
        #     - Time complexity O(nlogk), This will give an indication that sorting is involved for k elements.
        #     - Use already existing state to evaluate next state,
        #         Like, a set of k sorted numbers are only needed to be tracked. 
        #         When we are processing the next number in array, 
        #         then we can utilize the existing sorted state 
        #         and it is not necessary to sort next overlapping set of k numbers again.
        seen=[]
        for i in range(len(nums)-k):
            seen=nums[i:i+k]
            
