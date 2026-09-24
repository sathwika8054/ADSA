class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class Double_LL:
    def __init__(self):
        self.head = None

    def insert_begin(head, data):
        new_node = Node(data)
        new_node.next = head
        if head:
            head.prev = new_node
        return new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
    def count_nodes(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    def insert_at_a_position(self, data, pos):
        if pos < 1 or pos > self.count_nodes() + 1:
            print(f"Invalid position: {pos}")
            return
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        curr = self.head
        for _ in range(1, pos - 1):
            curr = curr.next
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node
    def delete_begin(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None
    def delete_end(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        if self.head.next is None:
            self.head = None
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.prev.next = None
    def traverse(head):
        curr = head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next 
        print("None")
head = None
head = Double_LL.insert_begin(head, 10)
head = Double_LL.insert_begin(head, 20)
head = Double_LL.insert_begin(head, 30)
head = Double_LL.insert_begin(head, 40)
head = Double_LL.insert_begin(head, 50)
print("Insertion at the beginning:")
Double_LL.traverse(head)
print()

dll = Double_LL()
dll.head = head

print("Insert at the end:")
dll.insert_end(80)
dll.insert_end(558)
Double_LL.traverse(dll.head)
print()

print("Insert 99 at position 4:")
dll.insert_at_a_position(99, 4)
Double_LL.traverse(dll.head)
print()

print("Delete from beginning:")
dll.delete_begin()
Double_LL.traverse(dll.head)
print()

print("Delete from end:")
dll.delete_end()
Double_LL.traverse(dll.head)
print()

