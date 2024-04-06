b = "Mundo"
a = "Hola"
c = a +" "+ b
print(c)

edad = 21
nom = "Mi nombre es Thomas y mi edad es de {}"
print(nom.format(edad))

a = "Somos los \"Vikingos\" del norte"
print(a)

lista = ['apple','banana','steve','apple']
print(lista)
print(len(lista))
print(lista[3])

if 'steve' in lista:
    print('Steve esta en la lista')

lista[1]='naranja'
print(lista)
lista.insert(2,'sandia')
print(lista)
lista2 = ['mango','piña','guayaba']

lista.extend(lista2)
print(lista)
lista.remove('apple')
print(lista)
lista.pop(0)
print(lista)
for x in lista:
    print(x)
num = [100,50,65,82,69]
num.sort()
print(num)
lista = lista.copy()
print(lista)