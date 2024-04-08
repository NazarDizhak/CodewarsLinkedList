def linked_list_from_string(s):
    data = s.split(' -> ')
    if len(data) == 1:
        return None

    head = Node(int(data[0]))
    current = head

    for value in data[1:]:
        if value == 'None':
            return head

        current.next = Node(int(value))

        current = current.next
