from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    
    new_node = Node()
    new_node.next = head
    
    current = new_node
    
    while current.next and current.next.next:
        node1 = current.next
        node2 = current.next.next
        
        current.next = node2
        node1.next = node2.next
        node2.next = node1
        
        current = node1
    
    return new_node.next