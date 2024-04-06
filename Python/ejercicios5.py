tupla = ('manzana','platano','sandia')
print(len(tupla))

estupla = ('lol',)

notupla = ('lol')
print(type(estupla))

print(type(notupla))
tupla1 = ('abc', 34, True, 40, 'Pinda',40,40)
print(tupla1)

x = ('rojo', 'amarillo', 'azul')
y = list(x)
y[1] = 'verde'
x = tuple(y)

print(x)
print(type(x))