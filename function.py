from collections.abc import Callable
from libraries import randint_list
from libraries import moyenne
def addition(a: float, b: float) -> float:
    """cette focntion permet d'addtionner deux nombres
    
     a float le premier nombre
     b le deuxieme nombre a additioner
     return float le resultat de l'addition """
    result = a + b

    return result

result = addition(123, 42)
print(result)

nb1 = 135
nb2 = 48

result = addition(nb1, nb2)
print(result)

def calculer(calcul1, calcul2, a, b, c,) -> float:
    result = calcul1(a, b)
    result = calcul2( result, c)

    return result

result = calculer(addition, addition, 123, 42, 14)
print(result)

my_list = randint_list(500, 1000, 6)
print(my_list)



lalist = randint_list(500, 1000, 6)
print(moyenne(lalist))


