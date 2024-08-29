# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Se define una lista de números, en este caso del 1 al 10

# Filtrado de números pares
numeros_pares = [] # Se crea una lista vacía que se mutará añadiendo números pares con un condicional
for numero in numeros: # Se itera la lista inicial
    if numero % 2 == 0: # Solo se toman en cuenta los números cuyo residuo entre 2 es 0 (pares)
        numeros_pares.append(numero) # Se añaden a la lista previamente definida

# Transformación: elevar al cuadrado
cuadrados = [] # Se crea una lista vacía que se mutará añadiendo números al cuadrado iterando
for numero in numeros_pares: # Se itera sobre la lista de números pares anterior
    cuadrados.append(numero ** 2) # Se unen a la lista de cuadrados los pares haciendo una operación en cada uno

# Suma de los números cuadrados
suma_cuadrados = 0 # Creación de una variable que inicia en 0
for cuadrado in cuadrados: # Iteración sobre cada número al cuadrado
    suma_cuadrados += cuadrado # Acumulación de la suma de cada número de la lista "cuadrados"

print(f"Suma de cuadrados de números pares: {suma_cuadrados}")
