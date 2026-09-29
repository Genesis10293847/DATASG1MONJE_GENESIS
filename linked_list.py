# Unit 3: Lists - Complete Singly Linked List (with head and tail)

class Node:
    def __init__(self, data):
        self.data = data      # 1. Data Field
        self.next = None      # 2. Next Pointer


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # ---------- Helpers ----------
    def is_empty(self):
        return self.head is None

    # ---------- Insertion ----------
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:            # empty list: head == tail
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head        # 1. link new node to current head
        self.head = new_node             # 2. move head to new node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node    # 1. link current tail to new node
            self.tail = new_node         # 2. move tail

    def insert_after(self, target, data):
        current = self.head
        while current is not None:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next   # save the old connection first
                current.next = new_node        # then relink
                if current is self.tail:       # inserted after last node
                    self.tail = new_node
                return True
            current = current.next
        return False

    # ---------- Deletion ----------
    def delete_from_beginning(self):
        if self.head is None:
            return False
        self.head = self.head.next
        if self.head is None:            # list became empty
            self.tail = None
        return True

    def delete_from_end(self):
        if self.head is None:
            return False
        if self.head.next is None:       # only one node
            self.head = None
            self.tail = None
            return True
        previous = self.head
        current = self.head.next
        while current.next is not None:
            previous = current
            current = current.next
        previous.next = None
        self.tail = previous
        return True

    def delete_value(self, value):
        if self.head is None:
            return False
        if self.head.data == value:      # first node (also handles only node)
            return self.delete_from_beginning()

        previous = self.head
        current = self.head.next
        while current is not None:
            if current.data == value:
                previous.next = current.next
                if current is self.tail:  # deleted the last node
                    self.tail = previous
                return True
            previous = current
            current = current.next
        return False

    # ---------- Traversal ----------
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # ---------- Searching ----------
    def search(self, target):
        current = self.head
        while current is not None:
            if current.data == target:
                return True
            current = current.next
        return False

    # ---------- Updating ----------
    def update(self, old_value, new_value):
        current = self.head
        while current is not None:
            if current.data == old_value:
                current.data = new_value
                return True
            current = current.next
        return False


# ---------- Demo ----------
if __name__ == "__main__":
    ll = LinkedList()

    print("Insert 30, 50, 100, 200 at the end:")
    for v in (30, 50, 100, 200):
        ll.insert_at_end(v)
    ll.display()

    print("\nInsert 5 at the beginning:")
    ll.insert_at_beginning(5)
    ll.display()

    print("\nInsert 70 after 50:")
    ll.insert_after(50, 70)
    ll.display()

    print("\nInsert 250 at the end:")
    ll.insert_at_end(250)
    ll.display()
    print("Head:", ll.head.data, "| Tail:", ll.tail.data)

    print("\nSearch for 65 and 100:")
    print("65 found?", ll.search(65))
    print("100 found?", ll.search(100))

    print("\nUpdate 70 to 75:")
    ll.update(70, 75)
    ll.display()

    print("\nUpdate 80 to 85 (does not exist):")
    if not ll.update(80, 85):
        print("Element 80 was not found.\nNo update was performed.")

    print("\nDelete from beginning:")
    ll.delete_from_beginning()
    ll.display()

    print("\nDelete value 75 (middle):")
    ll.delete_value(75)
    ll.display()

    print("\nDelete from end:")
    ll.delete_from_end()
    ll.display()
    print("Head:", ll.head.data, "| Tail:", ll.tail.data)

    print("\nDelete everything until empty:")
    while ll.delete_from_beginning():
        pass
    ll.display()
    print("Head:", ll.head, "| Tail:", ll.tail)