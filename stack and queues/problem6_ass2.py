
from  myLib.queue import Queue
class StringNonRepeat:
    def __init__(self):
        self.dict={}
        self.q=Queue()
    def AddInDictAndQueue(self,arr):
        for i in arr:
            if i in self.dict.keys():
                self.dict[i]=self.dict[i]+1
            else:
                self.dict[i]=1
                self.q.Enqueue(i)
    def PrintNonRepeat(self):
            while(self.q.Empty()is False):
                x=self.q[0]
                if x in self.dict:
                    if self.dict[x]==1:
                        print(x)
                    else:
                        self.q.Dequeue()
                        print(-1)
                        
x=StringNonRepeat()
x.AddInDictAndQueue(["a","a","b","c","c","d"])
x.PrintNonRepeat()
                
            