# = affectation
# addition/soustraction
ma_bite = 123 + 42
ma_bite = ma_bite + 16
ta_mere = 60
toi = ta_mere + ma_bite
print(toi)

# ** puissance ou ^ (pas en python)
# squrt (racine carré)
#// division entiere 
#% modulo = division eucludienne 
   
import random 
chibre = random.randint(1, 100)
print(chibre)
chibre = chibre % 2
print(chibre)

#operateur de comparaison
#egalité == "renvoie une valeur de type bouleen (true/false)"
#en gros savoir quelque chose sera egal a quelque chose
#ne pas confondre avec l'identité (en js) === le type de donnée et le meme (int/float) avec la même valeut
#il compare le type,puis compare les valeurs 

tyt = 1 == 1
print(tyt)


# operateur de grandeur 
tut = 123 < 42
tut =  12 <= 45
#<= vzeut dire plus petit ou egal et du coup >= plus grand ou egal 
#!= veut dire inegalité ou difference 

#les encadrements
# < > <= >=
pop = random.randint(0, 100)
cheh = 0 <= pop < 50
print(cheh)
chah = 0 >= pop > 50
print(chah)


#utilisation speciale des comparaisons de grandeurs 

lul = "abc" > "bcd"
print(lul)

#operateur "and"
result = True and False
print(result)
result = False and True
print(result)
result = False and False
print(result)
result = True and True
print(result)

a = random.randint(0, 1)
b = random.randint(0, 1)
rasult = a and b
print (a, b)
print(rasult)

#oerateur negation : "not"
# il faut mettre not false/or not true par exemple
#operateur "or"
result = True or False
print(result)
result = False or True
print(result)
result = False or False
print(result)
result = True or True
print(result)

a = random.randint(0, 1)
b = random.randint(0, 1)
rasult = bool(a) or bool(b)
print (a, b)
print(rasult)

counter = 10
while counter:
    print(f"{counter}")
    counter -= 1
#enleve -1 a chaque fois que while est executer 