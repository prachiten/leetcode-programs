class Node:
    def __init__(self,prev,value,next,key):
        self.value=value
        self.prev=None
        self.next=None
        self.key=key
class LRUCache:
    def __init__(self, capacity):
       self.capacity=capacity
        
    
        