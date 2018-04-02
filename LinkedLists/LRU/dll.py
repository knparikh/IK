class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.prev = None
        self.next = None

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        # update head and tail nodes if needed
        if self.head == node:
            self.head = next_node
        if self.tail == node:
            self.tail = prev_node

    def append_node(self, node):
        if self.head == None:
            self.head = node
        if self.tail == None:
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            # Update tail
            self.tail = node

    def remove_front_node(self):
        node = self.head
        if self.head:
            self.head = self.head.next # New head
            if self.head:
                self.head.prev = None
        if self.tail == node:
            self.tail = node.prev
        return node

    def print_values(self):
        curr = self.head
        while(curr):
            print curr.key,
            curr = curr.next
        print "\n"

if __name__ == "__main__":
    dll = DoublyLinkedList()
    nodes = []
    for i in range(6):
        nodes.append(Node(i, i))
        dll.append_node(nodes[i])

    dll.print_values()

    dll.remove_front_node()

    dll.print_values()

    dll.remove_node(nodes[3])

    dll.print_values()
    dll.remove_node(nodes[5])
    dll.print_values()

    dll.remove_front_node()
    dll.remove_front_node()
    dll.remove_front_node()

    dll.append_node(Node(6,6))
    dll.print_values()

