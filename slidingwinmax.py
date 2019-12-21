import collections

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        Given an array nums, there is a sliding window of size k 
        which is moving from the very left of the array to the very right.

        find the local maximum in each window and return the list of local maximums.
        """

        # using the dequeue
        if not nums: return []
        
        maxlist = []
        my_deque = collections.deque() 
        
        # for n in nums[:k]:
        #     # numbers in the deque are in descending order, which ensure the first number in the deque are the largest one
        #     while my_deque and my_deque[-1] < n:
        #         my_deque.pop()
        #     my_deque.append(n)
                
        # for r in range(k, len(nums)+1):
        #     maxlist.append(my_deque[0])
        #     if r < len(nums):
        #         # if the localmax in the previous window is the leftmost one,
        #         # need to remove it from the deque
        #         if nums[r-k] == my_deque[0]: 
        #             my_deque.popleft()
        #         while my_deque and my_deque[-1] < nums[r]:
        #             my_deque.pop()                 
        #         my_deque.append(nums[r])

        # the my_deque stores the indices
        for i in range(len(nums)):
            # remove numbers out of range k
            if my_deque and my_deque[0]<i-k+1:
                my_deque.popleft()
            # print("bf:",my_deque)
            # remove smaller numbers in k range as they are useless
            # make sure the my_deque only stores the inwindow position where numbers are larger than curr number
            while my_deque and nums[my_deque[-1]] < nums[i]:
                my_deque.pop()
            print(i,my_deque)
            
            # my_deque contains index
            my_deque.append(i)
            if i >= k - 1:
                maxlist.append(nums[my_deque[0]])
        return maxlist


sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3

print("Given the array: %s and k=%d"%(nums,k))
print("the list of the local maximum in each window of size k is: %s" % (sol.maxSlidingWindow(nums,k)))
# result: [3,3,5,5,6,7] 
