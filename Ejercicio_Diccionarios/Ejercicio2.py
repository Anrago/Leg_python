# Antonio Ramos Gonzalez
# Matricula:372576
# 10/05/2024
# Expo Diccionarios: Ejercicio 2

text = """El cuadrado del primer témino, más el doble del producto del primero por 
el segundo, más el cuadrado segundo"""

words = text.split()

element = {}

for word in words:
    if word in element:
        continue
    else:
        element[word] = words.count(word)

print(element)
