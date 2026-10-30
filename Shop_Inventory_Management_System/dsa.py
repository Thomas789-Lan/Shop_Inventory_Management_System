# ============================================================
# SHOP INVENTORY MANAGEMENT SYSTEM
# Combined TA-1 & TA-2 - Data Structures & Algorithms Project
# Team: Thomas Lalnuntluanga (251302044) & Puneet (251302026)
# ============================================================


# ============================================================
# ITEM CLASS
# ============================================================

class Item:

    # Constructor
    # Runs automatically when a new inventory item is created.
    def __init__(self, item_id, name, price, qty):
        self.item_id = int(item_id)
        self.name = str(name)
        self.price = float(price)
        self.qty = int(qty)

    # Display item details in console
    def display(self):
        print(f"ID: {self.item_id:<5} | Name: {self.name:<18} | Rs.{self.price:<8.2f} | Qty: {self.qty}")


# ============================================================
# PART 1: ARRAY-BASED INVENTORY (Dynamic Array / Python List)
# ============================================================

class ArrayInventory:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def insert_at_front(self, item):
        self.items.insert(0, item)

    def search_by_id(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def delete_by_id(self, item_id):
        for i, item in enumerate(self.items):
            if item.item_id == item_id:
                del self.items[i]
                return True
        return False

    def update_qty(self, item_id, new_qty):
        item = self.search_by_id(item_id)
        if item is not None:
            item.qty = max(0, int(new_qty))
            return True
        return False

    def get_all(self):
        return self.items

    def display(self):
        print("\n--- ARRAY INVENTORY ---")
        if not self.items:
            print("  (empty)")
            return
        for item in self.items:
            item.display()


# ============================================================
# PART 2: SINGLY LINKED LIST NODE & INVENTORY
# ============================================================

class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_front(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_end(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self.size += 1

    def search(self, item_id):
        current = self.head
        while current is not None:
            if current.item.item_id == item_id:
                return current.item
            current = current.next
        return None

    def delete_by_id(self, item_id):
        current = self.head
        prev = None
        while current is not None:
            if current.item.item_id == item_id:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        return False

    def update_qty(self, item_id, new_qty):
        item = self.search(item_id)
        if item is not None:
            item.qty = max(0, int(new_qty))
            return True
        return False

    def get_all(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.item)
            current = current.next
        return result

    def display(self):
        print("\n--- SINGLY LINKED LIST INVENTORY ---")
        if self.head is None:
            print("  No items in the list.")
            return
        current = self.head
        while current is not None:
            current.item.display()
            current = current.next


# ============================================================
# PART 3: DOUBLY LINKED LIST NODE & INVENTORY
# ============================================================

class DoublyNode:

    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_end(self, item):
        new_node = DoublyNode(item)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def delete_by_id(self, item_id):
        current = self.head
        while current is not None:
            if current.item.item_id == item_id:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                return True
            current = current.next
        return False

    def update_qty(self, item_id, new_qty):
        current = self.head
        while current is not None:
            if current.item.item_id == item_id:
                current.item.qty = max(0, int(new_qty))
                return True
            current = current.next
        return False

    def get_forward(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.item)
            current = current.next
        return result

    def get_backward(self):
        result = []
        if self.head is None:
            return result
        current = self.head
        while current.next is not None:
            current = current.next
        while current is not None:
            result.append(current.item)
            current = current.prev
        return result

    def display_forward(self):
        print("\n--- DOUBLY LINKED LIST (FORWARD) ---")
        if self.head is None:
            print("  No items in the list.")
            return
        current = self.head
        while current is not None:
            current.item.display()
            current = current.next

    def display_backward(self):
        print("\n--- DOUBLY LINKED LIST (BACKWARD) ---")
        if self.head is None:
            print("  No items in the list.")
            return
        current = self.head
        while current.next is not None:
            current = current.next
        while current is not None:
            current.item.display()
            current = current.prev


# ============================================================
# MAIN TERMINAL DASHBOARD (CLI MODE)
# ============================================================

def main():
    array_inv = ArrayInventory()
    singly_list = SinglyLinkedList()
    doubly_list = DoublyLinkedList()

    while True:
        print("\n" + "=" * 55)
        print("       SHOP INVENTORY MANAGEMENT SYSTEM (DSA)")
        print("=" * 55)
        print("1. Add Product Item")
        print("2. Display Inventory (Array + Singly List)")
        print("3. Search Item by ID")
        print("4. Update Item Quantity")
        print("5. Delete Item by ID")
        print("6. Doubly Linked List (Forward & Backward)")
        print("7. Exit")
        print("=" * 55)

        choice = input("Enter your choice: ")

        if choice == "1":
            item_id = int(input("Enter Item ID: "))
            name = input("Enter Product Name: ")
            price = float(input("Enter Unit Price (Rs.): "))
            qty = int(input("Enter Stock Quantity: "))

            array_inv.add_item(Item(item_id, name, price, qty))
            singly_list.insert_at_end(Item(item_id, name, price, qty))
            doubly_list.insert_at_end(Item(item_id, name, price, qty))
            print("Item added across all 3 data structures successfully!")

        elif choice == "2":
            array_inv.display()
            singly_list.display()

        elif choice == "3":
            item_id = int(input("Enter Item ID to search: "))
            found = singly_list.search(item_id)
            if found:
                print("Item Found!")
                found.display()
            else:
                print("Item not found.")

        elif choice == "4":
            item_id = int(input("Enter Item ID: "))
            new_qty = int(input("Enter New Quantity: "))
            if singly_list.update_qty(item_id, new_qty):
                array_inv.update_qty(item_id, new_qty)
                doubly_list.update_qty(item_id, new_qty)
                print("Quantity updated!")
            else:
                print("Item not found.")

        elif choice == "5":
            item_id = int(input("Enter Item ID to delete: "))
            if singly_list.delete_by_id(item_id):
                array_inv.delete_by_id(item_id)
                doubly_list.delete_by_id(item_id)
                print("Item deleted from all structures!")
            else:
                print("Item not found.")

        elif choice == "6":
            doubly_list.display_forward()
            doubly_list.display_backward()

        elif choice == "7":
            print("Thank you for using the Shop Inventory Management System!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()