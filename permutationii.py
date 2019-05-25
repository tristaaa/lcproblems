class Solution:
    def permuteUnique(self, nums):
        """
            return all possible unique permutations of the given collection of numbers.
            :type nums: List[int]
            :rtype: List[List[int]]
        """
        # method 1 [60 ms]
        # keep adding number to the position from 0 to len(li) to the previous result
        ret=[[]]
        
        for num in nums:
            newret=[]
            for li in ret:
                for i in range(len(li)+1):
                    newret.append(li[:i]+[num]+li[i:])
                    # avoid dupilcates by stop inserting a number after any of its duplicates
                    if i<len(li) and li[i]==num: break
            ret=newret
            
        return ret

        # method 2 [64 ms]
        # using dfs, backtrack the result
        def dfs(path, counter, ret):
            if len(path)==len(nums):
                ret.append(path)
            for x in counter:  
                # dont pick duplicates
                if counter[x] > 0:
                    counter[x] -= 1
                    dfs(path+[x], counter, ret)
                    counter[x] += 1

        ret = []
        hashmap = dict.fromkeys(nums,0)
        for num in nums:
            hashmap[num]+=1

        dfs([], hashmap, ret)

        return ret

        # method 3[124 ms]
        # swap the number in the array `nums`
        def dfs(nums, start, ret):
            if start>=len(nums):
                # print(nums)
                ret.add(tuple(nums))
            for i in range(start,len(nums)):
                if nums[i]==nums[start] and i>start:continue
                # print("fds:",nums)
                if i>start: 
                    nums[i],nums[start]=nums[start],nums[i]
                # print("sf:",nums,i,start)
                dfs(nums,start+1,ret)
                if i>start: 
                    nums[i],nums[start]=nums[start],nums[i]
               
        ret=set()
        dfs(nums,0,ret)
        return list(map(list,ret))


# test
sol=Solution()
nums=[2,2,1,1]
print("all possible unique permutations of the given collection: %s is: %s" % (nums, sol.permuteUnique(nums)))