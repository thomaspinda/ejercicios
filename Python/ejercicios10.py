"""""
username= input("Ingrese nombre de usuario: ")

try:
    print("Su nombre de usuario es: "+ username)
except NameError:
    print("ha ocurrido un error")
"""""
f = open("demo.txt","r")
print(f.read())
f.close()