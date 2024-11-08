class array(object):
    def __init__(self, capacity, fill_value = None): #capacidad del array
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self): #retorna la capacidad
        return len(self.items)

    def __str__(self): #
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):#para acceder a al index(indice)
        return self.items[index]

    def __setitem__(self, index, new_item): #para reemplaxar el valor en el index
        self.items[index] = new_item
