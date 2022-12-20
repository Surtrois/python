import random
def randint_list(lower: int, upper: int, count: int = 10,):
    numbers=[]

    for i in range(0, count):
        number = random.randint(lower, upper)
        numbers.append(number)
    
    return numbers






def moyenne(my_list:list):
    total = 0
    for i in range(len(my_list)):
        total += my_list[i]
    
    moyenne = total/len(my_list)
    return moyenne
    """Cette variable ne prend
en compte que des liste de nombres."""
