import random

if True: 
    print("c vrai")
    print("tellement vrai")

if False: 
    print("c faux")
    print("tellement faux")
#si if devient true ça effectue les truc,si c'est false bah non 


vente = random.randint(0, 1)

if vente == 0:
    print("il a dit oui")

if vente == 1:
    print("accepte moncon")

if vente:
    print("yeye")
else:
    print("nono")

#ou pour non tu peux faire if not

if not vente:
    print("c fo")
else: 
    print('c vrai')

mail = random.randint(0, 3)
if mail == 1:
    print("1 nouveau mail")
elif mail > 1:
    print(f"vous avez {mail} nouveau mails")
else: 
    print("ta pa dami lol")

#elif c else if 

fenetre_fermé = bool(random.randint(0 ,1))
electricity = bool(random.randint(0, 1))
print(f'{fenetre_fermé = }')
print(f'{electricity = }')

if fenetre_fermé:
    print("Bravo")
    print("le gouvernement est content")
elif not fenetre_fermé and electricity:
    print("les fenetre moncon")
    print("l'elec c bon")
elif fenetre_fermé and not electricity:
    print("fenetre super nickel")
    print("L'elec mon con")
else:
    print("oskour les fenetre")
    print("L'electricité ça va couter des sous")

cb = True
cash = True
print(f'{cb = }')
print(f'{cash = }')

if cb or cash:
    print("Possible de payer")
else:
    print ("Pas de sous")


#"or" ne permet pas de connaitre une des deux possibilités,uniquement si les deux sont vraies ou fausse 


ticket = random.randint(0 ,1)
vip = random.randint(0 ,1)
inscrit = random.randint(0 ,1)

print(f'{ticket = }')
print(f'{vip = }')
print(f'{inscrit = }')

if (vip or ticket) and inscrit:
    print("tu peux rentrer")
else:
    print("rentre pas")

#quand on melange or et and on doit TOUJOURS utiliser les parentheses 

product = random.randint(0 ,50)

if product > 20:
    print("+de20")
elif 5 < product <= 20:
    print("on a plus grand chose")
elif 0 < product <= 5:
    print("Presque a sec")
else:
    print("ya plus rien")