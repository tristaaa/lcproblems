class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ Solution: One-pass Hash Table,
            While we iterate and inserting elements into the table, 
            we also look back to check 
            if current element's complement already exists in the table

            Input: an array of integers, a target number
            Output: One unique list of indicies of two numbers such that their summation is equal to the target
            
            ** Notice: Assume that the result will be unique,
            we can use one element only once, 
            thus we must return two different indicies of the numbers in the input array 
        """
        dd = {}
        for i in range(len(nums)):
            numj = target - nums[i]
            if numj in dd and i!=dd[numj]:
                return [i, dd[numj]]
            dd[nums[i]] = i
         