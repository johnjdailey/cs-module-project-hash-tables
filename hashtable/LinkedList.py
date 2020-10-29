#LinkedList.py



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Runtime: O(1)

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    # Runtime:

    def insert_at_head_or_overwrite(self, node):
        existingNode = self.find(node.value)
        if existingNode is not None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node)

    # Runtime: O(n) n = number of nodes
    # Space complexity: constant O(1)

    def delete(self, value):
        curr = self.head

        # If the value is the head

        if curr.value == value:
            self.head = curr.next
            return curr
        
        # Reassign pointers

        prev = curr
        curr = curr.next

        while curr is not None:
            if curr.value == value:

                # Readdress the pointers

                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next
        return None


    
    # Runtime = O(n) n = number of nodes

    def find(self, value):
        curr = self.head

        # Loop through the list
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None
