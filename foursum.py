class Solution:
    def fourSum(self, nums, target):
        """
        Using the solution for three sum to solve four sum.

        Input: an array of n integers, a target number
        Output: all unique quadruplets(a,b,c,d) whose summation is equal to target number
        """

        # nums.sort()
        # ret=set()
        # for i in range(len(nums)-3):
        #     if i >=1 and nums[i]==nums[i-1]:
        #         continue
        #     targeti = target-nums[i]
        #     for j in range(i+1,len(nums)-2):
        #         if j>=i+2 and nums[j]==nums[j-1]:
        #             continue
        #         targetj = targeti-nums[j]
        #         dd={}
        #         for k in range(j+1,len(nums)):
        #             if targetj-nums[k] in dd:
        #                 ret.add((nums[i],nums[j],nums[k],nums[dd[targetj-nums[k]]]))
        #             dd[nums[k]]=k
        # return list(map(list,ret))

        # best solution: cursive version, base case: twosum using two pointers
        def findNSum(low, high, target, N, result, results):
            if high-low+1<N or N<2:
                return
            # early terminate
            if target<nums[low]*N or target>nums[high]*N:
                return
            # base case
            if N==2:
                while low<high:
                    tot = nums[low]+nums[high]
                    if tot<target:
                        low+=1
                    elif tot>target:
                        high-=1
                    else:
                        results.append(result+[nums[low],nums[high]])
                        while low<high and nums[low]==nums[low+1]:
                            low+=1
                        while low<high and nums[high]==nums[high-1]:
                            high-=1
                        low+=1
                        high-=1
            else: # recursive
                for i in range(low, high+1):
                    # if i==low or (i>low and nums[i]!=nums[i-1]):
                    findNSum(i+1, high, target-nums[i], N-1, result+[nums[i]], results)


        nums.sort()
        results = []
        findNSum(0, len(nums)-1, target, 4, [], results)
        return results


# test
sol = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
ret = sol.fourSum(nums,target)
print(ret) # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]



