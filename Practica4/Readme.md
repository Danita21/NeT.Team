# PREGUNTAS ADICIONALES

## 1. Teniendo en cuenta las características del ensamblador, ¿Cuál es la principal limitante que observan? Justifique su respuesta.

La principal limitante del ensamblador para la plataforma Hack radica en su naturaleza directa y la simplicidad del lenguaje simbólico que traduce. A diferencia de lenguajes de alto nivel, donde se pueden gestionar estructuras de datos complejas, abstracciones y operaciones sofisticadas, el ensamblador solo traduce instrucciones muy básicas (A-instrucciones y C-instrucciones) a código binario de 16 bits que la máquina Hack puede ejecutar directamente.
Justificación:
1. Simplicidad del Lenguaje Hack: El lenguaje ensamblador Hack es extremadamente sencillo, lo cual es útil para fines educativos, pero limita considerablemente la complejidad y el tipo de programas que se pueden escribir de manera eficiente. Cualquier tipo de abstracción debe ser manejada manualmente por el programador.
2. Resolución de Símbolos: Las etiquetas deben ser mapeadas a direcciones de memoria específicas, y la resolución de símbolos requiere múltiples pasadas sobre el código para garantizar que cada símbolo tenga un valor definido antes de ser utilizado en la traducción a binario.
3. Eficiencia: La falta de optimización es otra limitante. El ensamblador Hack traduce cada instrucción de manera bastante directa, sin aplicar optimizaciones que maximicen el uso del hardware.
4. Interactividad y Extensibilidad: El ensamblador no maneja multitarea ni características avanzadas como manejo de interrupciones.


# BONUS

## ¿Por qué es tan importante el ensamblador?

El lenguaje ensamblador constituye el primer intento de sustitución del lenguaje por uno más cercano al utilizado por los humanos. No obstante, el lenguaje ensamblador presenta la mayoría de los inconvenientes que tiene el lenguaje máquina: un repertorio muy reducido de instrucciones, el rígido formato de las instrucciones, la baja portabilidad y la fuerte dependencia del hardware.

Dado que el lenguaje ensamblador está fuertemente condicionado por la arquitectura del ordenador que soporta, los programadores no suelen escribir programas de tamaño considerable en ensamblador, sino que utilizan este lenguaje para afinar partes importantes de programas escritos en lenguajes de más alto nivel.

El lenguaje ensamblador sigue siendo importante, ya que ofrece al programador el control total de la máquina y como resultado genera un código compacto, rápido y eficiente, permite una interacción directa con el hardware, brindando control sobre los registros del procesador, la memoria y los dispositivos de entrada/salida y facilita la depuración a nivel de hardware, especialmente en situaciones donde el código de alto nivel no proporciona información suficiente para rastrear problemas complejos.

# Objetivo Práctica 6:

El objetivo es desarrollar un programa ensamblador que traduzca programas escritos en el lenguaje simbólico de ensamblador Hack a código binario, permitiendo que este código se ejecute en la plataforma de hardware Hack construida en proyectos previos.

# Proyecto 6: El Ensamblador.

El proceso para convertir un código ensamblador en código máquina sigue estos pasos:

-Inicialización:
Se crea un diccionario que asigna nombres simbólicos como 'SCREEN', 'SP', entre otros, a direcciones de memoria preestablecidas. Además, se asignan direcciones a los registros de 'R0' a 'R15', con valores que van del 0 al 15.
En este proyecto, el código en Python incluye este diccionario que se usa para asignar las direcciones correctas a los símbolos dentro del código ensamblador.

-Análisis del código:
Se analiza el código ensamblador utilizando un módulo especializado que realiza los siguientes pasos:

1. Creación de objetos parseadores: Se inicializa un objeto para cada línea del código, eliminando espacios y caracteres innecesarios, y se identifica el tipo de instrucción.

2. Detección del tipo de instrucción: Se clasifica la línea en comentarios, instrucciones A (comenzando con '@'), etiquetas (dentro de paréntesis), o instrucciones C.

3. Limpieza de la línea: Se eliminan comentarios y espacios innecesarios para facilitar el análisis posterior.

4. Extracción de componentes: A través de diferentes métodos, se extraen componentes como el valor, destino, operación, salto o etiqueta, según el tipo de instrucción.

-Conversión a código máquina:
El módulo codificador traduce las instrucciones ensambladoras en código binario. Para las instrucciones C, se convierte el destino, operación y salto a binario, mientras que en las instrucciones A, el valor se traduce a un binario de 15 bits. Los métodos funcionan así: Destino: Convierte la parte de destino de la instrucción C a su formato binario, usando un diccionario predefinido, operación: Traduce la operación de la instrucción C a binario, eliminando los espacios en blanco, salto: Convierte el salto de una instrucción C en su equivalente binario, valor: Transforma un número o una variable en binario de 15 bits. Si la variable no está en el diccionario, se le asigna un nuevo valor y se agrega al diccionario.

-Actualización de etiquetas y creación de la salida:
El diccionario se actualiza con las direcciones correspondientes a las etiquetas encontradas en el código. Para ello, se recorren las líneas ya analizadas, se detectan las etiquetas y se asignan sus direcciones basadas en un contador de instrucciones.
Los archivos de salida tienen la extensión ".hack". 

Al finalizar, el ensamblador se prueba con programas .asm, como el juego de pong, utilizando el entorno de nand2tetris.

# REFERENCIAS

[1] Project 06. (s/f). Nand2tetris. Recuperado el 4 de octubre de 2024, de https://www.nand2tetris.org/project06

[2] Software. (s/f). Uoc.edu. Recuperado el 4 de octubre de 2024, de https://cv.uoc.edu/moduls/XW02_79049_00373/web/main/m4/v2_3.html


