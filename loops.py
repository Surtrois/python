import random
kk = random.randint(0,10)

#while kk == 5:
#   print('ce message ne sera pas affiché')

#while kk == 0:
#  print('ce message sera affiché en boucle')

#else: print('Perdu')

counter = 10
while counter:
    print(f"{counter}")
    counter -= 1

counter = 1

while counter == 1:
    print(f"{counter}")
    counter += 1
#rajoute + 1 a chaque fois 

counter = 0

while counter != 1:
    print(f"{counter}")
    counter += 1

#!= veut dire different de 

for counter in range(0, 10):
    print(f"{counter =}")

fruits = ['abricot', 'pomme', 'cerise']
result = 'ananas' in fruits
print(result)
result = 'pomme' in fruits
print(result)

#permet de verifier si un truc est dans une liste 
for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):
    print(f'{i}: {fruit}')
#enumere ce qu'il y a dans la liste


#le 3 eme parametre de range permet de specifier l'increment (de 2 en 2 par ex)
for counter in range(0, 10, 2):
    print(f'{counter = }')


#compte a rebours 
for counter in range(10, 0, -1):
    print(f'{counter}')

print(fruits[::-1])

#les deux suivant sont equivalent 
for fruit in reversed(fruits):
    print(fruit)

for fruit in fruits[::-1]:
    print(fruit)