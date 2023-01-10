#pourquoi utiliser certaines fonctions et pas d'autres ?

path = "/home/foo"
filename = "document.txt"

file_path = path + '/' + filename
print(file_path) 

#imaginons que path soit fourni par l'utilisateur

path = "/home/foo/"
filename = "document.txt"

file_path = path + '/' + filename
print(file_path) 

#verifion si le dernier caractère de path est un slash ou non
#acceder au dernier caractere (-1)
if path[-1] == '/':
    file_path = path + filename
else: 
  file_path = path + '/' + filename  

#la fonction path.endswith('/') permet de faire le même test que path [-1] =='/':


#pourquoi est que parfois on appelle une fonction dans une autre fonction ?
#la lisibilité,optimisation du code
length = len(file_path)
print(length)


image = [[0, 17, 50, 137],
        [0, 17, 50, 137],
        [0, 17, 50, 157],
        [0, 17, 50, 107],
        [0, 17, 50, 127],
]

somm = 0
compteur = 0

for line in image:
    for column in line:
        if column <= 55:
            somm += column
            compteur += 1
moyenne = somm / compteur
print(f'{somm = }')
print(f'{compteur = }')
print(f'{moyenne = }')

users = [
    [1, 'foo@gmail.fr', 'admin', '123']
    [2, 'bar@gmail.fr', 'user', '1235']
    [3, 'baz@gmail.fr', 'user', '1320']
]

for i in range (0, 3):
    print (i)

for line in users:
    print(line)

for i, line in enumerate(users):
    print(i, line)