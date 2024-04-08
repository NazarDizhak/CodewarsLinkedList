def stringify(node):
    if node is None:
        return 'None'
    data = []
    while node is not None:
        data.append(str(node.data))
        node = node.next
    return ' -> '.join(data) + ' -> None'
