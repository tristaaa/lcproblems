class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxstack=[]
        self.maxvals=[]

    def push(self, x):
        '''Push element x onto stack.'''
        if not self.maxvals or x>=self.maxvals[-1][1]:
            self.maxvals.append((len(self.maxstack),x))
        self.maxstack.append(x)

    def pop(self):
        '''Remove the element on top of the stack and return it.'''
        curr = self.maxstack.pop()
        if curr==self.maxvals[-1][1]:
            self.maxvals.pop()
        return curr

    def top(self):
        '''Get the element on the top.'''
        return self.maxstack[-1]

    def peekMax(self):
        '''Retrieve the maximum element in the stack.'''
        return self.maxvals[-1][1]

    def popMax(self):
        '''Retrieve the maximum element in the stack, and remove it. 
            If you find more than one maximum elements, only remove the top-most one.'''
        # O(n)
        pos,curmax = self.maxvals.pop()
        if self.top()!=curmax:
            for i in range(pos,len(self.maxstack)-1):
                self.maxstack[i]=self.maxstack[i+1]
                if not self.maxvals or self.maxstack[i]>=self.maxvals[-1][1]:
                    self.maxvals.append((i,self.maxstack[i]))
                                    
        self.maxstack.pop()
        return curmax


# Note the functions other than `push` won't be called when stack is empty.

# Your MaxStack object will be instantiated and called as such:
obj = MaxStack()
obj.push(5)
obj.push(1)
obj.push(5)
param_1 = obj.top() # return 5
param_2 = obj.popMax() # return 5
param_3 = obj.top() # return 1
param_4 = obj.peekMax() # return 5
param_5 = obj.pop() # reutnr 1
param_5 = obj.top() # return 5
