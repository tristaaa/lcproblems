class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack=[]
        self.minvals=[]

    def push(self, x: int) -> None:
        self.minstack.append(x)
        if not self.minvals or self.minvals[-1]>=x:
            self.minvals.append(x)

    def pop(self) -> None:
        curr = self.minstack.pop()
        if self.minvals[-1]==curr:
            self.minvals.pop()

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return self.minvals[-1]


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print("inital min stack:",minStack.minstack)
print("curr min val in min stack:",minStack.getMin())   # Returns -3.
print("remove the top element in the min stack")
minStack.pop()
print("the curr top element in the min stack:",minStack.top())      # Returns 0.
print("curr min val in min stack:",minStack.getMin())   # Returns -2.
