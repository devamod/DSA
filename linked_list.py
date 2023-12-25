class Node:
    """
    An object for storing a single node of a linked list
    Models two attributes - data and the link to the next node in the list
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return (f"Node data: {self.data}")

class Linked_list:
    # Singly Linked List

    def __init__(self) -> None:
        self.head = None 

    def __repr__(self) -> str:
        """
        returns a Visual representation of a linked list
        Takes O(n) Times
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next

        return '-> '.join(nodes)
        

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current:
            current = current.next
            count += 1
        
        return count
    
    def add(self , data):
        """
        Adds a new Node containing data at head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self , key):
        """
        Return Found if key in the list or NOt Found if not in the list
        Takes O(n) times
        """
        current = self.head
        
        while current:
            if current.data == key:
                return "Found"
            
            current = current.next

        return "Not Found"
    
    def insert(self, key, index):
        """
        Inserts a new node at a given Index
        Takes O(n) times to find the node
        insertion takes O(1) times
        Takes overall O(n) times
        """

        if index == 0:
            self.add(key)

        current = self.head
        new = Node(key)
        position = index 

        while position > 1:
            current = current.next
            position -= 1

        new.next = current.next
        current.next = new

        return current
    
    def delete(self, key):
        """
        Deletes a node by its data
        Takes O(n) times
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                self.head = current.next
                found = True
            elif current.data == key:
                found = True
                previous.next = current.next
            else:
                previous = current
                current = current.next    
                
        if found:
            return 'Deleted'
        else:
            return 'Not in the List' 
        
    def remove(self , index):
        """
        Removes a Node at given index
        Takes O(n) times
        """

        current = self.head
        previous = None
        position = index

        if index == 0:
            self.head = current.next
            return 'removed'

        while position >= 1 and current: 
            previous = current
            current = current.next
            if position == 1:
                previous.next = current.next
                return 'removed'
            position -= 1
