class LinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 10

    def get_size(self):
        return self.size

    def is_size_empty(self):
        return self.size == 0

    # -----------------------------------
    # Add First
    # -----------------------------------
    def first_node(self, data):
        node = self.Node(data)
        self.add_first_node(node)

    def add_first_node(self, node):
        if self.is_size_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.size += 1

    # -----------------------------------
    # Add Last
    # -----------------------------------
    def last_node(self, data):
        node = self.Node(data)
        self.add_last_node(node)

    def add_last_node(self, node):
        if self.size == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    # -----------------------------------
    # Remove First
    # -----------------------------------
    def remove_first(self, data):
        if self.size == 0:
            return -1

        node = self.remove_first_node()
        return node.data

    def remove_first_node(self):
        node = self.head

        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            node.next = None

        self.size -= 1

        return node

    # -----------------------------------
    # Get First
    # -----------------------------------
    def get_first(self):
        if self.is_size_empty():
            return -1

        return self.get_first_node().data

    def get_first_node(self):
        return self.head

    # -----------------------------------
    # Get Last
    # -----------------------------------
    def get_last(self):
        if self.size == 0:
            return -1

        return self.get_last_node().data

    def get_last_node(self):
        return self.tail

    # -----------------------------------
    # Get At
    # -----------------------------------
    def get_at(self, idx):
        if self.is_size_empty() or idx > self.size:
            return -1

        node = self.get_at_node(idx)

        return node.data

    def get_at_node(self, idx):
        curr = self.head

        while idx > 0:
            curr = curr.next
            idx -= 1

        return curr

    def remove_last(self):
    if self.is_size_empty():
        return -1

    node = self.remove_last_node()
    return node.data


    def remove_last_node(self):
        node = self.tail
    
        if self.size == 1:
            self.head = self.tail = None
        else:
            second_last_node = self.get_at_node(self.size - 2)
    
            second_last_node.next = None
            self.tail = second_last_node
    
        self.size -= 1
    
        return node
