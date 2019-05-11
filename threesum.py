class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    """
        Using the solution for two sum to solve three sum.
        To save time, first sort the input array, 
        and skip the process of finding a triple (a,b,c) when 
        the 'a' element is already seen before.
        And use set to remove duplicate triples.

        Input: an array of n integers
        Output: all unique triples(a,b,c) where a+b+c=0
    """
        ret=set()
        nums.sort()
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

        # alternative solution: Using two pointers
        # ret = []
        # nums.sort()
        # for i in range(len(nums)-2):
        #     if nums[i]>0: break
        #     if i>=1 and nums[i]==nums[i-1]: continue

        #     low,high = i+1, len(nums)-1
        #     while low<high:
        #         currentsum = nums[i]+nums[low]+nums[high]
        #         if currentsum<0:
        #             low += 1
        #         elif currentsum>0:
        #             high -= 1
        #         else:
        #             ret.append([nums[i],nums[low],nums[high]])
        #             while low<high and nums[low]==nums[low+1]:
        #                 low+=1
        #             while low<high and nums[high]==nums[high-1]:
        #                 high-=1
        #             low+=1
        #             high-=1
        # return ret