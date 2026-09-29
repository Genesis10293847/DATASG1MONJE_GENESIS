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


# ---------- Menu Loop ----------
def read_int(prompt):
    """Keep asking until the user types a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def menu():
    ll = LinkedList()

    while True:
        print("\n===== LINKED LIST MENU =====")
        print("INSERT")
        print("  1. Insert at beginning")
        print("  2. Insert at end")
        print("  3. Insert after a value (middle)")
        print("DELETE")
        print("  4. Delete from beginning")
        print("  5. Delete from end")
        print("  6. Delete a value (middle)")
        print("OTHER")
        print("  7. Search")
        print("  8. Update")
        print("  9. Display")
        print("  0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            ll.insert_at_beginning(read_int("Value to insert: "))
        elif choice == "2":
            ll.insert_at_end(read_int("Value to insert: "))
        elif choice == "3":
            target = read_int("Insert after which value? ")
            data = read_int("Value to insert: ")
            if not ll.insert_after(target, data):
                print(f"{target} was not found. Nothing inserted.")
        elif choice == "4":
            if not ll.delete_from_beginning():
                print("List is empty.")
        elif choice == "5":
            if not ll.delete_from_end():
                print("List is empty.")
        elif choice == "6":
            value = read_int("Value to delete: ")
            if not ll.delete_value(value):
                print(f"{value} was not found. Nothing deleted.")
        elif choice == "7":
            value = read_int("Value to search: ")
            print(f"{value} was", "found." if ll.search(value) else "not found.")
        elif choice == "8":
            old = read_int("Old value: ")
            new = read_int("New value: ")
            if ll.update(old, new):
                print("Element updated successfully.")
            else:
                print(f"Element {old} was not found.\nNo update was performed.")
        elif choice == "9":
            pass  # display happens below
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

        # Show the list after every action
        print("\nCurrent list: ", end="")
        ll.display()
        if ll.head:
            print(f"Head: {ll.head.data} | Tail: {ll.tail.data}")
        else:
            print("Head: None | Tail: None")


if __name__ == "__main__":
    menu()