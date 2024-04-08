class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("Cannot split a list with less than two nodes")

    first = head
    second = head.next
    current_first = first
    current_second = second

    while current_second and current_second.next:
        current_first.next = current_second.next
        current_first = current_first.next
        current_second.next = current_first.next
        current_second = current_second.next

    current_first.next = None
    return Context(first, second)