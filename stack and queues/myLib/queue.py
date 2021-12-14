class Queue:
    def __init__(self):
        self.data = []

    def Enqueue(self, element):
        self.data.append(element)
        
    def Dequeue(self):
        if self.Empty() == False:
            return self.data.pop(0)
    def Empty(self):
        if (len(self.data)==0):
            return True
        else:
            return False
        
    def TotalElements(self):
        return len(self.data)
    
    def GetTop(self):
         return self.data[0]