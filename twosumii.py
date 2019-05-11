class Solution:
    def twoSum(self, numbers, target):
        """
            find the index(not zore-based) tuple where 
            the corresponding numbers add up to target number

            :type numbers: List[int], a sorted arrray
            :type target: int
            :rtype: List[int]
        """
        low,high=1,len(numbers)
        while low<high:
            tot=numbers[low-1]+numbers[high-1]
            if tot<target:
                low+=1
            elif tot>target:
                high-=1
            else:
                return [low,high]