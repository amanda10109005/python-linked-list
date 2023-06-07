#Custom Node & Linked List Class
class Node:
    def  __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList :
    def __init__(self):
        self.head = None

#menambahkan elemen list
    def add_to_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    #mengahapus elemen linked list
    def remove_front(self):
        if self.head is None:
            return
        
        self.head = self.head.next


    def remove_end(self):
        if self.head is None:
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    #mencetak isi linked list
    def print_linked_list(self):
        current = self.head
        while current:
            print(current.data, end =" ")
            current = current.next
        print()

#membuat dan mecetak list
linked_list = LinkedList()

linked_list.add_to_front(3)
linked_list.add_to_front(2)
linked_list.add_to_front(1)

linked_list.add_to_end(4)
linked_list.add_to_end(5)
linked_list.add_to_end(6)

print("Linked List Awal:")
linked_list.print_linked_list()    

#mengahapus dan mencetak list
linked_list.remove_front()
linked_list.remove_end()

print("Linked List Setelah Penghapusan:")
linked_list.print_linked_list()