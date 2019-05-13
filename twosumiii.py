class TwoSum:
    def __init__(self):
        self.hashmap = {}

    def add(self, number):
        """
        @Add the number to an internal data structure
        """
        self.hashmap[number] = self.hashmap.get(number,0)+1

    def find(self, value):
        """
        @Find if there exists any pair of numbers which sum is equal to the value
        """
        for num in self.hashmap:
            if value-num in self.hashmap:
                if value-num!=num or (value-num==num and self.hashmap[num]>1):
                    return True
        return False



# test
twoSum = TwoSum()
twoSum.add(1)
twoSum.add(1)
twoSum.add(3)
twoSum.add(5)
print("numbers:",twoSum.hashmap)
print("can add up to 2:",twoSum.find(2))
print("can add up to 4:",twoSum.find(4))
print("can add up to 7:",twoSum.find(7))