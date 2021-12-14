#Implement LRU Cache and also get and set function
class Node:
    def __init__(self,value,next=None,prev=None):
        self.value=value
        self.prev=prev
        self.next=next
        
    def increase(self):
        self.value += 1
        
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def AddingNodeAtFront(self,data):
        n=Node(data)

        if self.head is None:
            self.head=n
            print(f"value of head is {self.head.value}")
            self.tail=n
            print(f"value of tail is {self.tail.value}")
        else:
            self.head.prev = n
            n.next=self.head
            self.head=n
            print(f"value of head is {self.head.value}")
            print(f"value of tail is {self.tail.value}")
        
    # def AddingNodeAfterNode(self,data,prev_node):
    #     if prev_node == None:
    #         return
    #     n=self.createNode(data)
    #     n.next=prev_node.next
    #     prev_node.next=n
        
            
    def AddingNodeAtLast(self,data):
        n=Node(data)
        
        if self.head is None:
            self.head=n
            self.tail=n
            print(f"value of head is {self.head.value}")
            print(f"value of tail is {self.tail.value}")
        else:
            self.tail.next = n
            n.prev=self.tail
            self.tail = n
            print(f"value of head is {self.head.value}")
            print(f"value of tail is {self.tail.value}")
           
    
    # def DeleteNode(self,Node_to_delete):
    #     if self.head is None or Node_to_delete is None:
    #         return
    #     if self.head==Node_to_delete:
    #         self.head=Node_to_delete.next
    #         return
    #     if Node_to_delete.next!=None:
    #         Node_to_delete.prev.next=Node_to_delete.next
    #         return
    
    def PrintDoublyLinkList(self):
        last=self.head
        while(last!=None):
            print(last.value)
            last=last.next
        return
        
