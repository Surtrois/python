text1 = """Texte
multi-ligne
abc
foor
bar"""

print(text1)

text2 = "texte\foor\bar"

print(text2)

number = 123

#interpolation avec le f string
text3 = f"nombre =  {number}"
print(text3)

text5 = f"""
{{
    oui
}}
{{non}}"""

print(text5)

number1 = 3.14
text6 = "le nombre pi" + str(number1)
print(text6)

#.4f = 4 chiffres apres la virgule 
#tronquer un float dans une interpolation
number2 = 1/3
text7 = f"1/3 ~= {number2:.4f}"
print(text7)

# les interpolation acceptent les expressions 
text8 = f"1 + 1 = {1 + 1}"
print(text8)

#definit,puis nom de la fonction, 
def hello(name: str) -> None:
    print(f"Salut {name}")
    if name := "Henry":
        print("Wesh henry")

text9 = "lorem ipsum f f ff f f f f f f f f fff ipsum ffffffff"
#longeur d'une str
number4 = len (text9) 
print(number4)

#trouve la position d'une str dans une autre str
numbre10 = text9.find('ipsum') # rajoute number 10 + 1 apres ipsum pour trouver le deuxieme
print(numbre10)

#compte le nombre d'occurence d une str
number8 = text9.count ('f')
print(number8)

#remplace le texte 
print(text9.replace('f', 'b'))
print(text9)
#pour que le changement sois persistant 
text9 = text9.replace('f', 'v')
print(text9)

mienlist = text9.split()
print(mienlist)
print(len(mienlist))


#acces en lecture du 10 caractere

print(text9[0:10])

#10 en partant de la fin

print(text9[::-1])

#traiter un ellement sur 2
print(text9[::2])
