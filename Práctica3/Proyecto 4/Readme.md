# PREGUNTAS ADICIONALES

1. ¿Cuál es el objetivo de cada uno de esos proyectos con sus palabras y describa qué debe hacer para desarrollarlo?

Para el primer proyecto, el objetivo es construir todas las compuertas descritas en el Capítulo 2 (HalfAdder, FullAdder, etc.), hasta llegar a una Unidad Lógica Aritmética (ALU) de la computadora Hack (para realizar operaciones aritméticas). Todo esto únicamente haciendo uso de las compuertas creadas en el Proyecto 1 y las compuertas que se vayan creando en éste.

En el segundo proyecto, se construirá paso a paso una unidad de memoria de acceso aleatorio RAM a partir de compuertas DFF primitivas, compuertas construidas a partir de esas y compuertas construidas en prácticas anteriores. 
Para resolver estos proyectos, se empleará el software The Nand2tetris Software Suite, en donde se proporcionarán las herramientas y archivos necesarios para completar esta práctica.

2. Explique las principales diferencias entre la lógica aritmética y la lógica secuencial.

La lógica aritmética está dedicada a realizar operaciones matemáticas, como sumas, restas, multiplicaciones, utilizando circuitos combinacionales que ejecutan cálculos basados únicamente en las entradas actuales. Estos circuitos, como sumadores y unidades aritmético-lógicas (ALU), no mantienen estado, lo que significa que sus salidas cambian inmediatamente con las variaciones en las entradas. 
Por otro lado, la lógica secuencial se enfoca en almacenar y gestionar el estado de la información a lo largo del tiempo mediante elementos de memoria como flip-flops y registros. Estos circuitos dependen de eventos de reloj (clock) y del historial de entradas para determinar sus salidas, lo que permite la sincronización y la ejecución secuencial de operaciones. 

# BONUS
¿Qué tipo de unidades aritmético lógicas existen?

Algunos de los tipos de unidades aritmético lógicas (ALU) son:
-ALU Básica: Realiza operaciones aritméticas fundamentales como suma y resta, y operaciones lógicas básicas como AND, OR y XOR.

-ALU de N Bits: Opera con números de n bits, permitiendo realizar cálculos en palabras de diferentes tamaños, como 8, 16, 32 o 64 bits.

-ALU de Punto Flotante: Ejecuta operaciones aritméticas con números en punto flotante, como suma, resta, multiplicación y división.

-ALU SIMD (Single Instruction, Multiple Data): Optimizada para realizar la misma operación en múltiples datos simultáneamente, ideal para procesamiento paralelo.

-ALU de Cálculo de Enteros (Integer ALU): Especializada en realizar operaciones aritméticas y lógicas con números enteros, sin soporte para punto flotante.

-ALU de Cálculo de Enteros con Soporte para Operaciones Multiplicativas y Divisorias: Incluye funcionalidades adicionales para multiplicación y división, además de operaciones aritméticas básicas.

-ALU Personalizada o Especializada: Diseñada para realizar operaciones específicas requeridas por aplicaciones particulares o sistemas embebidos, con funcionalidades personalizadas.

# REFERENCIAS
[1] (S/f). Ecured.cu. Recuperado el 12 de septiembre de 2024, de https://www.ecured.cu/Unidad_Aritmético_Lógica#Tipos_de_ALU

[2] (S/f-b). Unican.es. Recuperado el 12 de septiembre de 2024, de https://ocw.unican.es/pluginfile.php/2410/course/section/2423/tema_04.pdf

[3] La Unidad Aritmética Lógica (ALU). (s/f). Algoreducation.com. Recuperado el 12 de septiembre de 2024, de https://cards.algoreducation.com/es/content/txMg2qW4/unidad-aritmetica-logica-alu

