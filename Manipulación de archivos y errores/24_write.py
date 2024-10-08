with open('./ejm.txt', 'w+') as file:
  for line in file:
    print(line)
  file.write('\n nuevas cosas en este archivo\n')
  file.write('otra linea\n')
  file.write(' otra  linea mas \n')