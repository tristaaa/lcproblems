class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    """
        Using the solution for two sum to solve three sum.
        To save time, first sort the input array, 
        and skip the process of finding a triple (a,b,c) when 
        the 'a' element is already seen before.
        And use set to remove duplicate triples.

        Input: an array of n integers
        Output: all unique triples whose summation is zero
    """
        nums.sort()
        ret=set()
        for i in range(len(nums)):
            if i>=1 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            dd={}
            for j in range(i+1,len(nums)):
                if target-nums[j] in dd:
                    ret.add((nums[i],nums[j],nums[dd[target-nums[j]]]))
                dd[nums[j]]=j
        return list(map(list,ret))