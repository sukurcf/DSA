class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = Node(head)

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_index(self, index, data):
        current = self.head
        previous = None
        while current is not None and index > 0:
            index -= 1
            previous = current
            current = current.next
        previous.next = Node(data, current)

    def get_length(self):
        node = self.head
        length = 1
        while node.next is not None:
            node = node.next
            length += 1
        return length

    def remove_at_index(self, index):
        if index == 0:
            self.head = self.head.next
            return
        if self.get_length() < index+1:
            print("index greater than length")
            return
        previous = None
        current = self.head
        while current is not None and index > 0:
            previous = current
            current = current.next
            index -= 1
        previous.next = current.next

    def print_ll(self):
        node = self.head
        lls = ""
        while node is not None:
            lls += str(node.data) + "--->"
            node = node.next
        print(lls)

    def print_middle_element(self):
        first = self.head
        second = self.head
        while second and second.next is not None:
            first = first.next
            second = second.next.next
        print(first.data)

    def delete_middle_element(self):
        first = self.head
        second = self.head
        previous = None
        while second and second.next is not None:
            previous = first
            first = first.next
            second = second.next.next
        previous.next = first.next

    def remove_duplicates(self):
        current_node = self.head
        previous_node = self.head
        current_element = current_node.data
        while current_node is not None:
            current_node = current_node.next
            if current_node is None:
                break
            if current_element == current_node.data:
                previous_node.next = current_node.next
            else:
                previous_node = current_node
                current_element = current_node.data

    def insert_at_end(self, data):
        data_node = Node(data)
        previous = None
        current_node = self.head
        while current_node is not None:
            previous = current_node
            current_node = current_node.next
        previous.next = data_node

    def reverse_linked_list(self):
        previous = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def add_number_to_linkedlist(self, number):
        self.reverse_linked_list()
        current = self.head
        carry = number
        while current is not None:
            current.data, carry = self.return_carry(current.data, carry)
            current = current.next
        if carry:
            self.head = Node(carry, self.head)
        self.reverse_linked_list()

    def return_carry(self, data, number):
        data += number
        rem = data - 9
        if data > 9:
            return data // 10, rem
        return data, 0

ll = LinkedList(9)
ll.insert_at_beginning(9)
ll.insert_at_beginning(9)
ll.insert_at_beginning(9)
ll.insert_at_beginning(9)
ll.insert_at_beginning(1)
# ll.print_ll()
# ll.remove_at_index(3)
# ll.print_ll()
# ll.delete_middle_element()
ll.print_ll()
ll.remove_duplicates()
ll.print_ll()
ll.add_number_to_linkedlist(1)
ll.print_ll()