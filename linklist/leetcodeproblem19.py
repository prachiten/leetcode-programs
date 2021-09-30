class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

    def printNode(self):
        print(self.value)

class SLL:
    def __init__(self):
        self.head=None

    def addNode(self, node):
        if isinstance(node, Node) == False:
            print("Did not receive a Node object")
            return self    ###### return self 

        if self.head is None:
            self.head = node
            return self   ###### return self

        nextnode = self.head
        while nextnode.next is not None:
            nextnode = nextnode.next
        
        nextnode.next = node    ####### modified this - it should have nextnode.next = node

        return self        

    def printList(self):
        res = None
        if self.head is not None:
            res=self.head
        else:
            print("List is empty")
        while res is not None:
            print(res.value)
            res=res.next

class Solution:
    def __init__(self, list1):
        self.l1 = list1
       
    def removeNthFromEnd(self,n):
        slow_ptr= self.l1.head
        fast_ptr= self.l1.head
        counter=1
        #corner cases
        if slow_ptr is None:
            return 

        if slow_ptr.next is None:
            l1=[]
            return slow_ptr
          
        while(counter<=n-1):
            fast_ptr=fast_ptr.next
            counter+=1
        while(fast_ptr.next is not None):
            fast_ptr=fast_ptr.next 
            if(fast_ptr.next is not None):
                slow_ptr=slow_ptr.next
            else:
                p=slow_ptr.next
                slow_ptr.next=p.next
                return p
        return 0
list1=SLL().addNode(Node(1)).addNode(Node(2)).addNode(Node(3)).addNode(Node(4)).addNode(Node(5))
list1.printList()
list1=SLL().addNode(Node(1)).addNode(Node(2))
list1.printList()
s = Solution(list1)
removedNode = s.removeNthFromEnd(1)
print("\n") 
removedNode.printNode()
print("\n")
s.l1.printList()
