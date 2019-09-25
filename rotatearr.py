class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead, with O(1) extra space.
        """
        # [72 ms]
        n=len(nums) 
        k %= n

        def reverse(arr, start, end):
            while start<end:
                # switch the position of the numbers pointed by start and end
                arr[start],arr[end] = arr[end],arr[start] 
                start+=1
                end-=1

        # first reverse the whole array
        reverse(nums,0,n-1)
        # then reverse the first k elements
        reverse(nums,0,k-1)
        # finally reverse the last n-k elements
        reverse(nums,k,n-1)

sol=Solution()
nums = [-1,-100,3,99,5,2,6,9]
nums_origin = nums.copy()
k=3
sol.rotate(nums,k)
print("rotate the given array: %s to the right by %d step(s), so the arr becomes: %s" %(nums_origin, k, nums) )