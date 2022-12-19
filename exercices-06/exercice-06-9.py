# exo 6.9
# Calculez la somme des nombres de la liste et affichez le résultat

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.9
sum = 0
for i in range(len(my_list)):
    sum += my_list[i]
print(sum)