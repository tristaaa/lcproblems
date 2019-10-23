class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        Given an array of integers and an integer k, 
        find out whether there are two distinct indices i and j in the array such that 
        ms[i] = nums[j] and the absolute difference between i and j is at most k.

        type nums: List[int]
        type k: int
        rtype: bool 
        """
        # method 1 [116 ms]
        # flag=False
        # seen={}
        # for i in range(len(nums)):
        #     if nums[i] not in seen:
        #         seen[nums[i]]=[i]
        #     else:
        #         seen[nums[i]].append(i)
        # for v in seen.values():
        #     if len(v)>1:
        #         minDis=v[-1]-v[0]
        #         for i in range(1,len(v)):
        #             if v[i]-v[i-1]<minDis:
        #                 minDis=v[i]-v[i-1]
        #         if minDis<=k:
        #             flag=True

        # return flag

        # method 2 [104 ms]
        seen={}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]]=i
            else:
                prevIdx = seen[nums[i]]
                if i - prevIdx<=k:
                    return True
                else:
                    seen[nums[i]]=i

        return False

sol = Solution()
nums = [1,2,3,1,2,4]
k=2
print("Given the array nums= %s, and a integer k=%s there are two distinct indices i,j where nums[i]==nums[j] and the absolute difference between i,j is at most k: %s" % (nums,k,sol.containsNearbyDuplicate(nums,k)))
