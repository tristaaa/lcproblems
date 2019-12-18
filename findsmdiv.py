class Solution:
    def smallestDivisor(self, nums, threshold):
        """
        Given an array of integers nums and an integer threshold, 
        we will choose a positive integer divisor and divide all the array by it and sum the result of the division. 
        Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

        Each result of division is rounded to the nearest integer greater than or equal to that element. 
        (For example: 7/3 = 3 and 10/2 = 5).

        It is guaranteed that there will be an answer.
        """

        # method[]
        # binary search
        # Given a divisor, if the result is larger than the threshold
        # then the divisor needed to increase; otherwise, the divisor needed to be smaller
        
        # initialize the divisor, the minimum divisor is 1 since it must be a positive integer and the maximum possible divisor is no larger than the max(nums), since it already provides the smallest summation
        
        l=1
        r=max(nums)
        while l<=r:
            m=(l+r)//2
            summation = sum((i+m-1)//m for i in nums)
            if summation>threshold:
                l=m+1
            else:
                r=m-1
        return l


sol = Solution()
numsl = [[1,2,5,9],[2,3,5,7,11]]
tl=[6,11]
for nums,threshold in zip(numsl,tl):
    print("Given the array:%s and the threshold:%d"%(nums,threshold))
    print("The smallest divisor that make the summation of each ceiling division no larger than the threshold is:%d \n"%sol.smallestDivisor(nums,threshold))
    # result 5
    # result 3
