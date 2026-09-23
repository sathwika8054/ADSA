'''
Double Linked list 
The data can be store in the node
nodes --> 3parts
1.data
2.prev
3.next
Algorithm 
1.create node
2.insert data
3.conections
4.traverse
 '''
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node1.next=node2
node2.next=node3
node3.next=node4 
node4.prev=node3
node3.prev=node2
node2.prev=node1

def traverse():
    curr=node1
    while curr:
        print(curr.data,end=" <-> ")
        curr=curr.next
    print("None")
def preivous():
    curr=node4
    while curr:
        print(curr.data,end=" <-> ")
        curr=curr.prev 
    print("None")

traverse()
preivous()
#insertion of a node at begining

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
def insert_begin(head,data):

    new_node=Node(data)
    new_node.next=head
    if head:
        head.prev=new_node

    return new_node
def insert_end(head,data):
    new_node=Node(data)
    if head is None:
        return new_node
    curr =head
    while curr.next:
        curr=curr.next
    curr.next=new_node
    new_node.prev=curr.next
    return head
def insert_at_post(head,data):
    

def traverse(head):
    curr=head
    while curr:
        print(curr.data,end=" <-> ")
        curr=curr.next 
    print("None")
head=None
head=insert_begin(head,10)
head=insert_begin(head,20)
head=insert_begin(head,30)
head=insert_begin(head,40)
head=insert_begin(head,50)
print("Insertion at the begin")

traverse(head)
print()

print("At the end of insertion ")
head=insert_end(head,100)
traverse(head)
print()


