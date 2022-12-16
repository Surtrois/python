fruits = ['mangue','pomme','tomate']
print(fruits)

#0 manipule le premier element,1 le deuxieme etc etc
fruits[0]
print(fruits[0])

lefruit = fruits[0]
print(lefruit)

#possible de changer l'interieur aussi

fruits[2] = "poire"
print(fruits)

#definir un index,puis on peux incrementer le += 1 pour passer a l'elements suivant 
index = 0
print(fruits[index])
index += 1
print(fruits[index])


combien = len(fruits)

if index < combien:
    print(f'{index =}')
    print(fruits[index])

#le dernier element c'est la taille de la list -1 (on commence a compter a partir de 0)
#toujours possible de retenir la taille de la liste!

#on peut utiliser un variable (index etc) pour trouver un element dans une liste
#possible d'augmenter ou diminuer avec -= ou +=


#ajouter un element
#supprimer un element
#inserer un element
fruits.append('datte')
print(fruits)
#supprime le fruit
del fruits[3]
#supprime le dernier element et peut le stocker dans une variable
fruits.pop()

#supprimer le premier et stocker
fruits.pop(0)
print(fruits)

#inserer un element (ne pas oublier qu'on demarre de 0) choisir 1 --> on se place entre 0 et 1 
fruits.insert(2, 'kiwi')
print(fruits)


