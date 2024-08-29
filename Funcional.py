# Creación y filtrado #

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Se define una lista de números, en este caso del 1 al 10
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
'''Para estos efectos, list convierte el objeto en una lista, mismo que a su vez es manipulado 
por filter, que filtra los elementos de la manera similar a una iteración con condicional. 
lambda funciona como una función simple y corta.'''

# Transformación #

cuadrados = list(map(lambda x: x**2, numeros_pares))
'''map aplica una función a cada elemento de la lista y devuelve una nueva con los resultados, en
esta ocasión toma cada número de números pares y aplica lambda (x^2) para finalmente devolver una
lista con resultados.'''

# Suma (con reduce del paquete functools) #

from functools import reduce
suma_cuadrados = reduce(lambda x, y: x + y, cuadrados)
'''reduce es utilizado para aplicar una función a una lista para que los elementos de la misma
se reduzcan a un solo valor, en este caso toma cada elemento de la lista y los va sumando de 2
en 2 (x+y) devolviendo así la suma de los cuadrados.
En este caso reduce acumula los valores y los combina en uno solo bajo una sumatoria hasta que,
finalmente, solo queda un número.'''

print(f"Suma de cuadrados de números pares: {suma_cuadrados}")