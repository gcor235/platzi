#leer un archivo linea por linea
"""with open('cuento.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())"""

#leer todas las lineas en una lista
"""with open('cuento.txt', 'r') as file: #para leer
    lines = file.readlines()
    print(lines)"""

#para añadir
"""with open('cuento.txt', 'a') as file:
    file.write("\n\nBy: Google")"""

#sobreescribir
with open('cuento.txt', 'w') as file:
    file.write("\n\nBy: Google")