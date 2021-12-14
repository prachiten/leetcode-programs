#Implement stack using queues
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
    
class Stack:
    def __init__(self):
        self.q1= Queue()
        self.q2= Queue()
    def Push(self,element):
        self.q1.Enqueue(element)
    def Pop(self):
        if self.q2.Empty() is True and self.q1.Empty() is False:
            while (self.q1.TotalElements()>1):
                self.q2.Enqueue(self.q1.Dequeue())
            print(self.q1.Dequeue())
            temp=[]
            temp=self.q2
            self.q2=self.q1
            self.q1=temp
            return
x=Stack()
x.Push(1)
x.Push(2)
x.Pop()
x.Push(3)
x.Pop()
x.Pop()
       
            
    
