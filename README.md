# CHECKPOINT 5
# Tabla de contenidos

  - [1. Introducción](#1-introducción)
  - [2. Condicionales en Python](#2-condicionales-en-python)
  - [3. Tipos de bucles (loops) en Python y utilidad](#3-tipos-de-bucles-loops-en-python-y-utilidad)
  - [4. List Comprehensions](#4-list-comprehensions)
  - [5. Argumentos en Python](#5-argumentos-en-python)
    - [Importancia de los argumentos](#importancia-de-los-argumentos)
    - [Tipos de argumentos](#tipos-de-argumentos)
  - [6. Función LAMBDA](#6-función-lambda)
  - [7. PIP (Python Package Index)](#7-pip-python-package-index)
___
## 1. Introducción

Como ya sabemos, Python es un lenguaje de programación increíble con una comunidad de programadores de las más fuertes, y es cada vez más usado en gran cantidad de ámbitos e industrias. Además, la sintaxis de Python es sencilla y cercana al lenguaje natural, lo que hace que éste sea uno de los mejores lenguajes para empezar a programar.

Esta guía reúne diferentes conceptos de Python de un nivel intermedio, por lo que para poder leerlo fácilmente es necesario tener unas bases de este lenguaje de programación.  

## 2. Condicionales en Python

Al igual que hacemos en la vida real, en Python los condicionales son proposiciones que nos ayudan a tomar decisiones. Para ello deben cumplirse, o no, ciertas circunstancias o escenarios, y en base a ello, elegiremos una opción. Por ejemplo, si el día está nublado y la temperatura es menor de 15 grados, tendremos que llevar paraguas y ropa de abrigo para salir, pero si está lloviendo y además hace frío, podremos optar por quedarnos en casa, o por salir con paraguas y ropa de abrigo. 

En el ámbito de la programación, los condicionales son instrucciones que se le dan a un programa para que **ejecute un bloque de código u otro si se cumplen determinados requisitos**. De este modo, puede adaptarse a distintas situaciones e incluso responder ante usos o consultas inusuales.  

El software entiende cada condición como verdadera o falsa, y actúa según dicha evaluación. Para explicar las circunstancias que se valoran, se hace uso de los operadores de Python, especialmente de los **lógicos** —cuando hay que comprobar más de un requisito a la vez—, y los de **comparación** —cuando la condición es única—.

A continuación se muestran todos los operadores de comparación: 

*  == Igual
* != Diferente
* <> Diferente (obsoleto)
*  Mayor que >
*  Mayor o igual a >=
*  Menor que <
*  Menor o igual a <=
 
Existen tres tipos de sentencias condicionales, entre ellas: 

Sentencia **if**: ejecuta el bloque de código en caso de que se cumpla una condición.

Sentencia **else**: ejecuta el bloque de código si la condición es falsa.

Sentencia **Elif**: Si hay más de una condición, se debe comprobar en una secuencia de veces que las condiciones anteriores fueron falsas

Nota importante: **Else** siempre se usa con el último condicional, como en el siguiente ejemplo: 


```Python
age = 55

if age < 25:
    print(f"I'm sorry, {age} is under 25 years old")
elif age > 100:
    print(f"I'm sorry, {age} is over 100 years old")
else:
    print(f"You're good to go, {age} fits in the range to rent a car")
  ```

Aquí se muestran ejemplos de condicionales usando operadores de comparación: 

```python
x = 5

if x > 10:
    print("x es mayor que 10")
else:
    print("x es menor o igual a 10")
```

En el ejemplo anterior se utilizan los operadores de comparación > < para definir si un número `x` es mayor, menor o igual a 10. El siguiente código usa el operador ***mayor o igual que** para definir si la nota alcanza la nota de aprobación, o por el contario es reprobatoria. 

```python
puntuación = 85

if puntuación >= 50:  

    print("¡Has aprobado!")  

else:  

    print("Has reprobado.")  
```
¿Qué sucede cuando necesitamos que se cumplan dos condiciones? Por ejemplo, si necesitamos que el nombre de usuario y la contraseña coincidan. Para ello, podemos incorporar el operador `AND` a nuestro sistema. Ahora bien, si lo que necesitamos es que haya dos condiciones y cualquiera de las dos se cumpla, usaremos el operador `OR`. El operador OR funciona analizando la expresión completa y comprobando primero el lado izquierdo. Si es verdadero, simplemente omite todo lo que está a la derecha, ya que para que la operación OR se considere verdadera, basta con que un lado coincida y el otro sea verdadero.

Aquí un ejemplo de condicionales usando operadores lógicos: 

```python
username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
    print('Access permitted')
else:
    print('Not allowed')
```
Es importante destacar la sintaxis de los condicionales, pues si no se respeta la indentación (espaciado o sangría en el inicio de la línea), Python detectará un error y nos indicará que algo falla en la sintaxis. En Python se recomienda una indentación de cuatro espacios entre cada declaración, como se muestra en los ejemplos anteriores. Además, como se observa el bloque de código, después de cada condicional deben escribirse dos puntos (:). 

Para concluir, ¿por qué son esenciales las sentencias condicionales en la programación lógica?

* Porque permiten tomar decisiones de forma sencilla

Imagina que estás trabajando en una aplicación de comercio electrónico. Las sentencias condicionales ayudan a decidir qué sucede cuando un usuario agrega artículos a su carrito o completa un pago. Este proceso de toma de decisiones constituye la base de la programación lógica.

* Porque permiten la creación de aplicaciones robustas

En ciencia de datos, los algoritmos suelen basarse en lógica condicional para realizar predicciones o procesar conjuntos de datos. Por ejemplo, las sentencias condicionales son fundamentales en los modelos de aprendizaje automático para árboles de decisión, clasificación y filtrado de datos ruidosos.

* Porque mejora los fundamentos de la programación

Aprender las sentencias condicionales es como aprender los fundamentos de la programación. Una vez que domines esto, otros conceptos como los bucles, las funciones y la recursión serán más fáciles de entender. Estos conceptos los profundizaremos en esta guía, más adelante. 

En resumen, los condicionales permiten crear aplicaciones robustas y resolver problemas de manera eficiente, ya que permiten implementar estructuras de programación lógicas que **imitan los procesos de toma de decisiones humanas**. Desde la automatización de tareas hasta el desarrollo de algoritmos avanzados, las sentencias condicionales son un componente esencial de los fundamentos de la programación.

## 3. Tipos de bucles (loops) en Python y utilidad

Los bucles (también llamados iteraciones o loops) son estructuras que permiten ejecutar un bloque de código múltiples veces. Son fundamentales en programación porque automatizan tareas repetitivas y permiten procesar colecciones de datos de forma eficiente. Los bucles están 

Un buen ejemplo de su utilidad es el siguiente: imagina que necesitas enviar un email a 1000 clientes. Sin bucles, tendrías que escribir el mismo código 1000 veces. Con un bucle, escribes el código una vez y lo ejecutas automáticamente tantas veces como necesites.

Su sintaxis general sería como se muestra a continuación:

```python
while condicion:
    ejecuta las intrucciones de este bucle
```

Python ofrece dos tipos principales de bucles:

* Bucle **for / in**: itera sobre una secuencia (lista, tupla, string, range, etc.). El bucle o loop se repetirá tantas veces como elementos haya en la lista, tupla, string, range, etc.
* Bucle **while**: repite mientras una condición sea verdadera. Al desarrollar el programa debemos indicarle cuándo debe detenerse, de lo contrario se repite hasta el infinito y podría dar errores o bugs.
  
Ejemplo de loop for / in:

```Python
players = {
  '2b': 'Altuve',
  '3b': 'Bregman',
  'ss': 'Correa',
  'dh': 'Gattis'
}

for position, player in players.items():
  print('Position', position)
  print('Player', player)
  ```
Ejemplo de loop while: 

```python
cantidad = 0
while cantidad < 10:
    print(cantidad)
    cantidad += 1
```
Este código imprimirá los números del 0 al 9 en la consola. La variable cantidad comienza en 0 y se va incrementando en 1 hasta que llega a ser mayor o igual a 10, lo que hace que se deje de cumplir la condición.

Dentro de los bucles en Python, también podemos utilizar las sentencias `break` y `continue` para controlar el flujo de ejecución.

Termina el bucle y ejecuta el bloque de código que está después del bucle.

Veamos un ejemplo utilizando break para salir de un bucle for:

```python
frutas = ["manzana", "banana", "cereza", "sandía", "uva"]

for fruta in frutas:
    print(fruta)
    if fruta == "sandía":
        break
```

En este caso, el bucle for imprimirá cada fruta de la lista hasta que llegue a “sandía”, momento en el cual se ejecutará break y el bucle se interrumpirá.

Por otro lado, la función `continue` se utiliza para saltar una iteración y continuar con la siguiente, sin ejecutar el código que queda de la iteración actual. Por ejemplo, si queremos imprimir todos los números en la lista excepto el número 3, podemos usar la función continue para saltar ese número:

```python
my_list = [1, 2, 3, 4, 5]

for num in my_list:
  if num == 3:
    continue
  print(num)

# Salida:
# 1
# 2
# 4
# 5
```

Otra manera de evitar loops infinitos es usar un **contador**. En lugar de confiar en una variable para cambiar de valor, podemos usar un contador para contar el número de iteraciones que se han realizado y detener el loop cuando llega a un número específico. Aquí hay un ejemplo:

```python
counter = 0
while counter < 10:
    print(counter)
    counter += 1
```

También se pueden crear loops con rangos. Para ello se usa la función `range`. Por ejemplo, si queremos crear una cuenta regresiva podemos usar el siguiente código: 

```python
>>> for count in range(10, 0, -1):
...     print(count)
>>> print("¡Despegue!")
10
9
8
7
6
5
4
3
2
1
¡Despegue!
```

## 4. List Comprehensions

Una List Comprehension es esencialmente un conjunto de bucles `for-in` y condicionales que se pueden colocar en una sola línea de código. En otras palabras, es una forma simplificada de escribir el mismo código y más fácil de leer, y con el mismo resultado.

Esta forma de usar bucles o loops nos permite condensar en una línea, lo que en la forma tradicional hacemos en cuatro.

Ejemplo: 

```python
# Forma tradicional
squares = []
for number in range(1, 6):
     squares.append(number ** 2)
squares
#resultado = [1, 4, 9, 16, 25]
 
# Con list comprehension
squares = [number ** 2 for number in range(1, 6)]
squares
#resultado = [1, 4, 9, 16, 25]
```
## Sintaxis básica

La sintaxis general es:

```python
[nueva_expresion for elemento in secuencia if condicion]
```
- nueva_expresion: lo que quieres agregar a la nueva lista.
- elemento: cada valor de la secuencia original.
- secuencia: la colección de datos a recorrer.
- condicion (opcional): filtro para incluir solo ciertos elementos.

En este otro ejemplo, vamos a crear una lista con los todos los múltiplos de 2 entre 0 y 10 usando el método tradicional y el método de list comprehensions: 

```python
# Método tradicional
lista = []
for numero in range(0,11):
    if numero % 2 == 0:
        lista.append(numero)
print(lista)
```
```python
# Con comprensión de listas
lista = [numero for numero in range(0,11) if numero % 2 == 0 ]
print(lista)

#resultado = [2,4,6,8,10]
```

En ciertas ocasiones, las comprensiones son útiles no sólo por que pueden ser escritas en una sola línea de código, sino que también pueden llegar a ser más rápidas que otros métodos. Es muy importante por lo tanto medir su tiempo de ejecución para saber si son una buena elección.

## 5. Argumentos en Python

Los argumentos son los valores que acompañan a una función en Python. Una función está representada por la palabra ***def*** un parámetro que la define y los ***argumentos*** que van entre paréntesis, tal y como se observa en el siguiente ejemplo: 

```python
def un_parámetro («argumentos»)
Representación de una función
```
En los paréntesis, es decir, en los argumentos, podemos establecer cualquier tipo de valor, desde strings, listas, e incluso otras funciones, aunque también puede ser que el paréntesis esté vacío, lo cual significa que tiene un argumento por defecto o un argumento indefinido. Aquí un ejemplo de ello: 

<img width="927" height="194" alt="undefined_argument" src="https://github.com/user-attachments/assets/44dd92c3-53b5-4491-9ea9-987ad310d8c6" />


Los argumentos permiten que la función realice cálculos o procesos personalizados según los datos proporcionados o los valores asignados. 

```python
def sumar(numeros):
         return sum(numeros)
print(sumar([1, 2, 3, 4, 5])) # Salida: 15
````
En este caso, los valores asignados son los números desde el 1 hasta el 5 y el cálculo esperado es la suma de todos ellos, siendo el resultado 15, como se observa en el comentario del código.

Como ya se ha mencionado, existen varios tipos de argumentos: 

### Tipos de argumentos

1.  Argumentos predeterminados
2.  Argumentos en paquete o `*args`
3.  Argumentos de palabra clave o ***kwargs***
4.  Argumentos posicionales
   
El primer tipo de argumento se denomina ***predeterminado***. Éstos son los principales aspectos que debemos comprender acerca de éste tipo de argumento: 
* Los argumentos predeterminados son valores que se proporcionan al definir las funciones.
* El operador de asignación =se utiliza para asignar un valor predeterminado al argumento.
* Los argumentos predeterminados se vuelven opcionales durante las llamadas a la función.
* Si proporcionamos un valor a los argumentos predeterminados durante las llamadas a funciones, este anula el valor predeterminado.
* La función puede tener cualquier número de argumentos predeterminados.
* Los argumentos predeterminados deben ir después de los argumentos no predeterminados.

La sintaxis para usar **argumento empaquetado** consiste en comenzar con un asterisco y luego la convención común es nombrar la lista de argumentos como args. Es la convención común y la mejor práctica. Sin embargo, no se trata de un concepto ni una palabra clave obligatorios.

Se pueden usar otros nombres para el grupo de argumentos, sin que altere el comportamiento de la función, pero es común usar simplemente el nombre args, que es la abreviatura de "argumentos", precedida por un asterisco, de la siguiente manera: `(*args)`. En el siguiente ejemplo se sustituye *args por otro nombre: 

<img width="927" height="197" alt="arg_paquete" src="https://github.com/user-attachments/assets/fc4259c2-99ae-48ef-8ad0-99cdb1b434b1" />

También existen los argumentos de palabra clave o ***kwargs*** devuelven un diccionario, puesto que usan palabras clave. Se escribe `**kwargs`.

Una de las principales diferencias entre trabajar con argumentos con nombre y el desempaquetado tradicional. Al "desempaquetar" una lista de argumentos tradicional, se devuelve como una ***tupla***. Al desempaquetar argumentos con nombre, se devuelven como un ***diccionario***. Se trata de un enfoque lógico, ya que un argumento con nombre necesita un conjunto de claves y valores asociados, que es la definición misma de un diccionario. Por lo tanto, este es uno de los elementos clave que debemos recordar. Aquí un ejemplo de `**kwargs`.

<img width="928" height="167" alt="kwargs" src="https://github.com/user-attachments/assets/83e0fc39-86af-41e2-aaa1-079d0d2d2d6f" />


Por último, tenemos los ***argumentos posicionales*** que se definen como valores de una función que deben llamarse en un orden específico, donde el primer argumento corresponde al primer parámetro, el segundo al segundo, y así sucesivamente. Son obligatorios y deben coincidir en número y posición con la definición de la función para evitar errores.

Aquí hay un ejemplo donde construimos una función sencilla para generar un nombre completo:

```python 
def full_name(first_name, last_name):
    return f'{first_name} {last_name}'  # Combina el nombre y el apellido

print(full_name('Anna', 'Brown'))       # Imprime 'Anna Brown'
```
### Importancia de los argumentos

* Reutilización de código: Permiten que las funciones sean flexibles y reutilizables.
* Menos repetición: Evitan escribir múltiples versiones de una función con diferentes valores.
* Mayor claridad: Los argumentos bien definidos hacen que el código sea más legible.
* 
## 6. Función LAMBDA

La mayoría de los lenguajes de programación modernos y de propósito general incluyen este tipo de construcción denominado `lambda`.

Lambda es una herramienta que permite encapsular una función, generalmente una función pequeña, y luego pasarla fácilmente a otras funciones. 

Las funciones lambda son expresiones anónimas, lo que significa que no tienen nombre a menos que se asignen explícitamente a una variable. También son usadas para tareas rápidas y temporales sin necesidad de `def`. Se aplican comúnmente en ordenamiento `(sort)`, filtrado `(filter)` y mapeo `(map)`. También se les conoce como funciones anónimas o expresiones lambda.

Una expresión lambda consiste en la palabra clave lambda seguida de una lista de ar­gu­me­n­tos, dos puntos y una única expresión (“ex­pre­s­sion”). En cuanto se llama la función lambda, se pro­po­r­cio­na la expresión con los ar­gu­me­n­tos y se evalúa:

```python
lambda argument: expression
```
A di­fe­re­n­cia de la sentencia `def`, `lambda` inicia una expresión que no debe contener ninguna sentencia. La expresión lambda toma uno o más ar­gu­me­n­tos y devuelve una función anónima. Si se llama a la función lambda generada, se hará una eva­lua­ción de la expresión contenida con los ar­gu­me­n­tos pasados y se devolverá el resultado.

```python
greeting = lambda name: f"Hi, {name}"
       
return greeting
```

Otro ejemplo muy usual de lambda, como hemos indicado arriba, es con la función `filter`. En este código, comenzamos definiendo un conjunto de números. A continuación, creamos una función lambda para comprobar si un número es par. La función filter aplica esta función lambda al conjunto denominado "numbers". A continuación, imprimimos la lista de números pares identificados por la función filter.

```python
# Usar filter con la función lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # imprime la lista tras el filtro

# resultado = [2, 4, 6, 8]
````

## 7. PIP (Python Package Index)

Pip es el gestor de paquetes de Python.
Sirve para instalar, actualizar y eliminar librerías externas que amplían lo que Python puede hacer.

En términos técnicos, pip descarga e instala paquetes desde el repositorio oficial de Python: Python Package Index (conocido como PyPI).

¿Para qué se usa en la práctica?

Python por sí solo trae funciones básicas.
Cuando necesitas funcionalidades más avanzadas, usas librerías que instalas con pip.

Ejemplos:

| Librería | Para qué sirve                 |
| -------- | ------------------------------ |
| NumPy    | cálculo numérico y matrices    |
| Pandas   | análisis de datos              |
| Requests | hacer peticiones a páginas web |
| Flask    | crear aplicaciones web         |

Para entender mejor que es PIP, pensemos en Python como un teléfono nuevo.

PIP sería la App Store.

Con PIP puedes instalar "apps" (librerías) que añaden nuevas capacidades a Python.

Como dato curioso, existe también un "término secreto" que se usa para referirse a PIP como "la tienda de quesos" o "Python Cheese Shop" (en inglés). Esta denominación tiene que ver con un sketch de los Monty Python (admirados por el creador de este lenguaje de programación). En dicho sketch, el actor John Cleese intenta comprar quesos en una tienda gestionada por Michael Palin, pero el tendero no tiene absolutamente nada de queso, a pesar de que la tienda se llama "National Cheese Emporium".

¿Y qué tiene que ver esto con el lenguaje Python y PIP? Pues que en los inicios de PyPI, el repositorio estaba prácticamente vacío, sin paquetes disponibles, lo que recordaba al sketch donde la tienda nunca tenía quesos, adoptando el sobrenombre de "The Cheese Shop".

En PIP los paquetes y módulos están estructurados de tres maneras: uno con acceso directo; otro donde están integrados en el lenguaje principal, pero aun así es necesario importarlos; y un tercero donde se trata de bibliotecas de terceros que deben instalarse manualmente.

En la siguiente imagen se observan algunas de las librerías más populares de PIP. 


<img width="882" height="1024" alt="librerías_python" src="https://github.com/user-attachments/assets/96ba4056-4772-4bea-aaa4-09309145e3fc" />








 


