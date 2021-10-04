from multiprocessing import Pool
import time
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None


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

    def printNode(self):
        res = None
        if self.head is not None:
            res=self.head
        else:
            print("List is empty")
        while res is not None:
            print(res.value)
            res=res.next


class Solution():
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        
    def addNumbersInLists(self):
        head1 = self.list1.head
        head2 = self.list2.head
        carry=0
        l3=SLL()
       
        while (head1!=None or head2!=None):
            if (head1 is None and head2 is None ):
                sum=0
            elif (head1 is None and head2 is not None):
                sum=head2.value+carry
                
            elif (head2 is None and head1 is not None):
                sum=head1.value+carry
                
            else:
                sum=head1.value+head2.value+carry
            digitsum=sum%10
            carry=sum//10
            sumnode = Node(digitsum)
            l3.addNode(sumnode)
            
            head1=head1.next if head1 else None
            head2=head2.next if head2 else None
        #end while
        return l3 #####  return list here
def main(data1, data2):
    start_time= time.time()
    list1 = SLL()
    for d in data1:
        list1.addNode(Node(d))
    #list1.printNode()
    list2 = SLL()
    for d in data2:
        list2.addNode(Node(d))

    #list2.printNode()
    #nums=[list1,list2]
    sol = Solution(list1, list2).addNumbersInLists()
    end_time=time.time()
    print(end_time-start_time)
    return sol

if __name__ == "__main__":
    data_pairs =  [ [[2,3,4], [4,5,6]], 
                    [[5,1,4], [3,2,8]] ]

    parallel = True
    if parallel == False:
        for dp in data_pairs:
            main(dp[0], dp[1]).printNode()
    else:
        p=Pool(len(data_pairs))
        res=p.starmap(main, data_pairs)
        for r in res:
            r.printNode()
    
    



##added this call - have not tested the program




            

            
            
            



