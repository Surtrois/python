# exo 6.10
# Calculez la moyenne des nombres de la liste et affichez le résultat

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.10

sum = 0
for i in range(len(my_list)):
    sum += my_list[i]
    moyenne = sum/len(my_list)
print(moyenne)