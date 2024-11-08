from node import Node

class singlylinkedlist:
    def _init_(self):
        self.tail = None
        self.size = 0

    def append(self, data):
        node =Node(data)

        if self.tail == None:
            self.tail = node #si esta vacio tomara el valor ingresado
        else:
            current = self.tail 

            while current.next: #  se iran corriendo los espacios de memoria
                current = current.next

            current.next = node

        self.size +=1

    def size(self):
        return str(self.size)
    
    def iter(self):
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data): #para borrar un valor
        current = self.tail
        previous = self.tail

        while current: #para organizar los otros valores
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data 
                
            previous = current 
            current = current.next

    def search(self, data): # para buscar un nodo
        for node in self.iter():
            if data == node: 
                print(f"dato {data} encontrado!")

    def clear(self): #para limpiar la lista
        self.tail= None
        self.head = None
        self.size = 0
