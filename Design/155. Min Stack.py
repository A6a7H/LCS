'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: 'int'):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.stack.append((x, curMin));

        
    def pop(self):
        return self.stack.pop()[0]
    
    
    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][0]

        
    def getMin(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()