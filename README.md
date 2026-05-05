# CHECKPOINT 5
___
## 1. Condicionales en Python
Los condicionales son instrucciones que se le dan a un programa para que **ejecute un bloque de código u otro si se cumplen determinados requisitos**. De este modo, puede adaptarse a distintas situaciones e incluso responder ante usos o consultas inusuales.  

El software entiende cada condición como verdadera o falsa, y actúa según dicha evaluación. Para explicar las circunstancias que se valoran, se hace uso de los operadores de Python, especialmente de los **lógicos** —cuando hay que comprobar más de un requisito a la vez—, y los de **comparación** —cuando la condición es única—.

Los principales condicionales en Python son ***if***, ***else*** y ***elif***. El primero se refire al primer condicional que debe cumplirse, en caso contrario, se aplica el condicional **else**, y si hay más de dos condiciones se utilizará **elif**, tantas veces como condicionales existan. Else siempre se usa con el último condicional, como en el siguiente ejemplo: 


```Python
age = 55

if age < 25:
  print(f"I'm sorry, {age} is under 25 years old")
elif age > 100:
  print(f"I'm sorry, {age} is over 100 years old")
else:
  print(f"You're good to go, {age} fits in the range to rent a car")
  ```

## 2. Tipos de bucles (loops) en Python y utilidad
Los bucles (también llamados iteraciones o loops) son estructuras que permiten ejecutar un bloque de código múltiples veces. Son fundamentales en programación porque automatizan tareas repetitivas y te permiten procesar colecciones de datos de forma eficiente.

Un buen ejemplo de su utilidad es el siguiente: imagina que necesitas enviar un email a 1000 clientes. Sin bucles, tendrías que escribir el mismo código 1000 veces. Con un bucle, escribes el código una vez y lo ejecutas automáticamente tantas veces como necesites.

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

## 3. List Comprehensions

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

## 4. Argumentos en Python

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


### Importancia de los argumentos

* Reutilización de código: Permiten que las funciones sean flexibles y reutilizables.
* Menos repetición: Evitan escribir múltiples versiones de una función con diferentes valores.
* Mayor claridad: Los argumentos bien definidos hacen que el código sea más legible.

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

## 5. Función LAMBDA

La mayoría de los lenguajes de programación modernos y de propósito general incluyen este tipo de construcción denominado `lambda`.

Lambda es una herramienta que permite encapsular una función, generalmente una función pequeña, y luego pasarla fácilmente a otras funciones. 

Las funciones lambda son expresiones anónimas, lo que significa que no tienen nombre a menos que se asignen explícitamente a una variable. También son usadas para tareas rápidas y temporales sin necesidad de `def`. Se aplican comúnmente en ordenamiento `(sort)`, filtrado `(filter)` y mapeo `(map)`. Su sintaxis es `lambda argumentos: expresión`. También se les conoce como funciones anónimas o expresiones lambda.

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

## 6. PIP

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








 


