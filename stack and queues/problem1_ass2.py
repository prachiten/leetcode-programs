class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)
        
    def pop(self):
        if self.isEmpty() == False:
            self.data.pop()
    
    def top(self):
        if self.isEmpty() == False:
            return self.data[-1]
        else:
            return None
    
    def elementCount(self):
        return len(self.data)
    
    def isEmpty(self):
        return len(self.data) == 0
#end definition
    

# print next greater element in array
def NextGreater(arr):
    stack=Stack()
    result=[]
    size=len(arr)
    for i in range(size-1,-1,-1):
        if stack.isEmpty():
            result.append(-1)
        else:
            while(stack.elementCount() > 0 and stack.top()<arr[i] ):
                stack.pop()
            if stack.isEmpty():
                result.append(-1)
            else:
                result.append(stack.top())
        stack.push(arr[i])
    return result
print (NextGreater([13,7,6,12]))
        
        
    
    