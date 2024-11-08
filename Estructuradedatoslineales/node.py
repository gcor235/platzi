class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Creacion de 3  nodos diferentes
node1 = None
node2 = Node("A", None)
node3 = Node("B", node2)

node1 = Node("C", node3)