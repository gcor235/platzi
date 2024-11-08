file = open('./ejm.txt')
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

for line in file:
  print(line)

file.close()

with open('./ejm.txt') as file:
  for line in file:
    print(line)