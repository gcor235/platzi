from array import array


class Grid(object):
    def __init__(self, rows, columns, fill_value = None):
        self.data = array(rows)
        for row in range(rows):
            self.data[row] = array(columns, fill_value)

    def get_height(self): #retorna la altura
        return len(self.data)

    def get_width(self): #retorna el numero de columnas
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "

            result += "\n"

        return str(result)
