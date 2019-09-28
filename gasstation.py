class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        gas[i] is the amount of gas at station i you can fuel;
        cost[i] is the amount of gas cost to go from station i to i+1
        Return the starting gas station's index if you can travel around the circuit 
        once in the clockwise direction, otherwise return -1.
        If there exists a solution, it is guaranteed to be unique
        Both input arrays are non-empty and have the same length and all elements are non-negeative

        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        # [64 ms]
        # Basic idea: if A cannot reach B(the first station A cannot reach),
        # then for any station C between A and B, C cannot reach B
        # (since if A can reach C, then the tank at C must >=0, 
        # which means the lack of gas would be much more from C to B than from A to B)
        # so if we fail to reach the station i+1 from the currnet start, 
        # we can skip the starting point between start and i, these stations cannot be the viable start station

        # first starting at station start=0
        start,tank,total=0,0,0

        for i in range(len(gas)):
            # record the tank when reached the station i+1
            tank += gas[i]-cost[i]
            # if car cannot reach station i+1 from station `start`
            # restart from station i+1
            if tank<0:
                # total records the amount of gas needed
                # to go from station 0 to station i+1
                total-=tank
                start=i+1
                tank=0

        return start if tank-total>=0 else -1

