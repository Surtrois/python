#scope ou la portée des variables

foo = 123
def bar():
    foo = 42
    print(foo)

print(foo) 
bar()
print(foo)

#constructeur
class Voiture:
    def __init__(self):
        self.passagers = 0
        self.vitesse = 0
    
v = Voiture
print(v.passagers)
print(v.vitesse)
v.passagers = 3
v.vitesse = 50
print(v.passagers)
print(v.vitesse)

#v esr une instance de la classe voiture
#v est un objet de la classe voiture
#quand j'appelle ma classe voiture,je le lance tout de suite 


#methode getter
#permet de lire la variable
def getPassagers(self):
    return self.Passagers

#setter
#permet de modifier une variable
def setPassagers(self, passagers):
    if type(passagers) is int and passagers >= 0 and passagers <= 4:
        self.passagers = passagers
    
