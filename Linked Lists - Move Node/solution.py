class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    # Your code goes here.
    # Remember to return the context.
    if source is None:
        raise ValueError("No node to move")
  
    s1, s2 = source, source.next
    s1.next = dest
  
    return Context(s2, s1)
