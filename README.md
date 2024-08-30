# Resumen de la presentación
## Introducción
En esta presentación, se explorará en profundidad el paradigma de la programación funcional, un modelo de desarrollo que ha ganado reconocimiento por su eficacia en la gestión de aplicaciones que requieren alta concurrencia y fiabilidad. En un mundo donde la eficiencia en el procesamiento de datos y la escalabilidad son esenciales, la programación funcional ofrece herramientas valiosas y se ha vuelto crucial en el desarrollo de sistemas distribuidos y aplicaciones de tiempo real.

La presentación comenzará definiendo la programación funcional como un paradigma donde las computaciones se estructuran alrededor de la evaluación de expresiones en lugar de la ejecución de comandos. Este enfoque se distingue por su uso de funciones puras y estructuras de datos inmutables, lo que lleva a una mayor previsibilidad y facilidad de prueba del código. Los principios fundamentales incluyen la inmutabilidad, que elimina los cambios de estado y las variables globales; funciones puras, que garantizan el mismo resultado bajo las mismas condiciones sin efectos secundarios; transparencia referencial, que permite reemplazar expresiones con sus valores sin cambiar el comportamiento del programa; y funciones de primera clase, que pueden ser asignadas a variables, pasadas como argumentos, o retornadas por otras funciones.
## Profundización y evolución
Se profundizará en cómo la programación funcional se compara con otros paradigmas, como el imperativo y el orientado a objetos. Se discutirán cómo la inmutabilidad facilita el manejo del estado y reduce los efectos secundarios, mejorando la testabilidad y fiabilidad del código. Aunque presenta desafíos, como una curva de aprendizaje más empinada y dificultades en tareas que gestionan estado, como las interfaces de usuario, los beneficios a largo plazo en términos de mantenibilidad y seguridad del código son significativos.

Además, se revisará la evolución histórica de la programación funcional, desde sus raíces en el cálculo lambda propuesto por Alonzo Church, pasando por lenguajes influyentes como Lisp y ML, hasta llegar a modernos como Haskell y Scala. Este recorrido histórico permite apreciar cómo las características funcionales han sido integradas en lenguajes multiparadigma, ampliando su adopción y adaptabilidad en diversos contextos de programación.
## Práctica
En términos de aplicaciones prácticas, se discutirá cómo lenguajes específicos como Haskell, Scala y Erlang se utilizan en diferentes sectores. Haskell, por ejemplo, es ampliamente valorado en la academia y la investigación por su enfoque puramente funcional, que es ideal para proyectos que requieren alta fiabilidad y precisión. Scala, por otro lado, es preferido en el desarrollo de aplicaciones empresariales y sistemas de alto rendimiento, combinando funcionalidad con orientación a objetos para facilitar la escalabilidad y el manejo de la concurrencia. Erlang se destaca en telecomunicaciones y sistemas distribuidos, aprovechando su capacidad para manejar múltiples operaciones simultáneamente con alta disponibilidad.

También se abordarán los desafíos de implementar la programación funcional, especialmente en entornos donde dominan otros paradigmas. Se explorarán estrategias efectivas para superar estos obstáculos, como la educación continua y la implementación de arquitecturas híbridas que integran lo mejor de los paradigmas funcional e imperativo.
### Ejemplo Práctico:
Se presenta un ejemplo donde se define una lista de números, se filtran los números pares, se elevan al cuadrado y se realiza la suma de ellos, con una salida esperada de "Suma de cuadrados de números pares: 220".
## Programación Imperativa vs. Funcional:
### Imperativa: 
Se caracteriza por ser más explícita y detallada en el control del flujo del programa, utilizando mutabilidad y funciones sencillas. 
### Funcional: 
Se enfoca en la inmutabilidad, utiliza funciones predefinidas, y es adecuada para transformaciones complejas como en big data, aunque tiene una curva de aprendizaje más pronunciada y puede implicar un mayor consumo de memoria.

## Consideraciones de la Programación Funcional:
* Las funciones puras permiten paralelización.
* Mayor consumo de memoria en algunas situaciones.
* Fragmentación en su adopción.
* Curva de aprendizaje más alta en comparación con la programación imperativa.

## Comparación con Otros Paradigmas:
### Imperativa: 
Control detallado del flujo del programa.
### Funcional: 
Ideal para transformaciones complejas y procesamiento continuo de datos.
### POO (Programación Orientada a Objetos): 
Enfocada en modelos con interacción, común en entornos empresariales.
## Conclusión
Finalmente, se concluirá esta presentación reflexionando sobre el futuro de la programación funcional. Dado que los sistemas y aplicaciones modernas enfrentan retos cada vez más complejos, especialmente en áreas de alta concurrencia y sistemas distribuidos, el paradigma funcional se perfila como una solución cada vez más relevante. Su capacidad para mejorar la claridad, eficiencia y seguridad del desarrollo de software es una promesa de un futuro donde la programación funcional juega un papel central en la evolución de nuestras tecnologías.
# Guía para ejecutar los scripts Funcional.py e Imperat.py

Este documento proporciona instrucciones para ejecutar los scripts `Funcional.py` e `Imperat.py`. Ambos scripts están escritos en Python y se espera que sean ejecutados en un entorno compatible con Python 3.x.

## Requisitos Previos

Antes de ejecutar los scripts, asegúrate de tener instalado lo siguiente:

- Python 3.x: Puedes descargar la última versión de Python desde [python.org](https://www.python.org/downloads/).
- Un terminal o consola de comandos (CMD, PowerShell, Terminal de Linux o macOS).

## Instalación

### 1. Clonar o descargar los archivos

Descarga ambos archivos (`Funcional.py` e `Imperat.py`) y guárdalos en un directorio local de tu elección.

### 2. Configurar el entorno

Asegúrate de que Python esté instalado correctamente. Puedes verificarlo ejecutando el siguiente comando en tu terminal o consola:

```sh
python --version
```

## Ejecución de los Scripts
### 1. Funcional.py
Para ejecutar el script (`Funcional.py`), abre una terminal o consola de comandos, navega hasta el directorio donde se encuentra el archivo y ejecuta:

```sh
python Funcional.py
```
### 2. Imperat.py
Para ejecutar el script (`Imperat.py`), sigue el mismo procedimiento:

```sh
python Imperat.py
```
