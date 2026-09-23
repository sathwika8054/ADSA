'''
what is ds:the way we 
managing'
organizing
sorting the data '''
'''the datastructure is organized into two types
premitive
non premitive
'''
#premitive
'''int,str,float'''
#non primitive
'''linear(list,linkedlist,stacks,quese)'''
'''non linear (trees,graps)'''
#linked list
'''they are three types 
1.single linked list 
algorith
1.creating the node 
2.insert the data 
3.connection btw the nodes 
4.Traverse each node
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
def traverse():
    curr=node1
    while curr:
        print(curr.data,end="->")
        curr=curr.next
    print("None")
traverse()
'''
Operations
1.Insertion
   Insertion at beging
   Insertion at end
   Insertion after a particular node

2.Deletion
    Deletion at the being
    Deletion at the end 
    Deletion after a particular node 

3.traverse
4.updation
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_begin(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node
def traverse(head):
    curr = head
    while curr:
        print(curr.data, end="->")
        curr = curr.next
    print("None")
head = None
head = insert_begin(head, 10)
head = insert_begin(head, 20)
traverse(head)
'''
Singly Linked List: 
Algorithm:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(40)
node4=Node(50)
node1.next=node2
node2.next=node3
node3.next=node4
def traverse():
    curr=node1
    while curr:
        print(curr.data,end="-->")
        curr=curr.next
    print("None")
traverse()


Operations:
1. Insertion
   a. Insertion at the begin
   b. Insertion at the end 
   c. Insertion after a particular node
2. Deletion
   a. Deletion at the begin
   b. Deletion at the end 
   c. Deletion after a particular node
3. Traverse
4. Updation
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_begin(head,data):
    new_node=Node(data)
    new_node.next=head
    return new_node

def deletion_begin(head):
    if head is None:
        print("Error")
        return None 
    new_head=head.next
    del head 
    return new_head

def insert_end(head,data):
    new_node=Node(data)
    if head is None:
        return new_node
    curr=head
    while curr.next:
        curr=curr.next
    curr.next=new_node
    return head

def deletion_end(head):
    if head is None or head.next is None:
        print("Error")
        return None 
    curr=head
    while curr.next.next:
        curr=curr.next
    del_node=curr.next
    curr.next=None
    del del_node 
    return head

def insert_at_pos(node,data):
    if node is None:
        print("Error")
        return 
    new_node=Node(data)
    new_node.next=node.next
    node.next=new_node

def traverse(head):
    curr=head
    while curr:
        print(curr.data,end="-->")
        curr=curr.next 
    print("None")
head=None 
head=insert_begin(head,10)
head=insert_begin(head,20)
head=insert_begin(head,30)

print("Insertion at beginning")
traverse(head)
print()

print("Insertion at the end")
insert_end(head,100)
traverse(head)
print()

print("Insertion after the Node")
insert_at_pos(head,1000)
traverse(head)
print()

print("Deletion at beginning")
head=deletion_begin(head)
traverse(head)
print()

print("Deletion at the end")
head=deletion_end(head)
traverse(head)
print()