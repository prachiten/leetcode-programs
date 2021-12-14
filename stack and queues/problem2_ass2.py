#implement queues using 2 stacks
class Stack:
    def __init__(self):
        self.arr=[]
    def push(self,element):
        self.arr.append(element)
    def pop(self):
        if len(self.arr)!=0:
            return(self.arr.pop())
            
    
    def PrintElement(self):
        for i in self.arr:
            print(i)
    def empty(self):
        if(len(self.arr)==0):
            return True
        else:
            return False
            
class Queue:
    
    def __init__(self):
        self.arr=[]
        self.s1= Stack()
        self.s2= Stack()
       
    def Enqueue(self, element):
        self.s1.push(element)
        
        
    def Dequeue(self):
        if(self.s2.empty() is True and self.s1.empty() is False):
            while (self.s1.empty() is False): 
                self.s2.push(self.s1.pop())
            print(self.s2.pop())
            return
        
        if (self.s1.empty() is True):
            print(self.s2.pop())
            return
        if self.s1.empty() is False and self.s2.empty() is False:
            while(self.s1.empty() is False):
                self.s2.push(self.s1.pop())
            if self.s1.empty() is True:
                while(self.s2.empty() is False):
                    self.s1.push(self.s2.pop())
            print(self.s1.pop())
            return
x=Queue()
x.Enqueue("a")
x.Enqueue("b")
x.Enqueue("c")
x.Dequeue() 
x.Dequeue()
x.Enqueue("d")
x.Dequeue() 
x.Dequeue()

    
    
        



