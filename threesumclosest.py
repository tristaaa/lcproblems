class Solution:
    def threeSumClosest(self, nums, target):
        """
            Find the sum of three integers in the array which is closest to the target.

            :type nums: List[int]
            :type target: int
            :rtype: int
        """
        nums.sort()
        tot = nums[0]+nums[1]+nums[2]
        diff = abs(target - tot)

        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            while l<r:
                currsum = nums[i]+nums[l]+nums[r]
                currdiff = abs(target - currsum)

                if currdiff<diff:
                    tot = currsum
                    diff = currdiff

                if currsum<target:
                    l+=1
                elif currsum>target:
                    r-=1
                else:
                    return currsum

        return tot


# test
nums=[-1, 2, 1, -4]
target = 1
sol = Solution()
print("closest sum to the target(%d)= %d" % (target, sol.threeSumClosest(nums,target)))