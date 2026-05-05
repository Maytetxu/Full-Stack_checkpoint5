#Ejercicio 1. Loop for-in
def loop_over_string():
    name = 'Mayte'
    for letter in name:
        print(letter)

loop_over_string()

#Ejercicio 2. Función suma
def suma(a, b, c):
    return a+b+c

resultado = suma (1, 2, 3)
print(suma(1,2,3))

#Ejercicio 3. Función lambda
suma = lambda a, b, c: a + b + c

#Ejercicio 4. Condicionales
nombre = 'Enrique'

lista_nombres = ('Jessica', 'Paul', 'George', 'Henry', 'Adán')

if nombre in lista_nombres:
    print("El nombre está en la lista")
else:
    print("El nombre NO está en la lista")