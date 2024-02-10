class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, head: Node) -> None:
        self.head = head
        self.len = 1

    def append(self, node: Node) -> None:
        current_node = self.head
        while(current_node.next != None):
            current_node = current_node.next
        current_node.next = node
        self.len += 1
        return
    
    def insert(self, node: Node, index: int) -> None:
        if index == 0:
            node.next = self.head
            self.head = node
            self.len += 1
            return       
          
        current_node = self.head
        current_index = 0
        while(current_node.next != None):
            if current_index == index - 1:
                node.next = current_node.next
                current_node.next = node
                self.len += 1
                return
            current_node = current_node.next
            current_index += 1
        if current_node.next == None:
            if index == current_index + 1:
                node.next = None
                current_node.next = node
                self.len += 1
            else:
                raise Exception("Index out of list boundry")
        return
    
    def delete(self, index: int) -> None:
        # Deleting Head Node
        if index == 0:
            self.head = self.head.next
            self.len -= 1
            return
        
        current_node = self.head
        current_index = 0
        while(current_node.next != None):
            if current_index == index-1:
                current_node.next = current_node.next.next
                self.len -= 1
                return
            current_node = current_node.next
            current_index += 1

        if current_node.next == None and index > current_index:
            raise Exception("Index out of list boundry")
        return
    
    def search(self, value:int) -> int:
        current_node = self.head
        current_index = 0
        while(current_node.next != None):
            if current_node.value == value:
                return current_index
            current_node = current_node.next
            current_index += 1
        if current_node.next == None and current_node.value == value:
            return current_index
        else:
            raise Exception("Value Not Found")     

    def get(self, index: int) -> int:
        current_node = self.head
        current_index = 0
        while(current_node.next != None):
            if current_index == index:
                return current_node.value
            current_node = current_node.next
            current_index += 1
        if current_node.next == None and current_index == index:
            return current_node.value
        return -1  
    
    def reverse(self) -> None:
        first_head = self.head
        while(first_head.next != None):
            current_head = self.head
            self.head = first_head.next
            first_head.next = first_head.next.next
            self.head.next = current_head
        return

    def print_values(self) -> None:
        current_node = self.head
        while(current_node.next != None):
            print(current_node.value)
            current_node = current_node.next
        if current_node.next == None:
            print(current_node.value)
        return
    
    def get_len(self) -> int:
        return self.len


