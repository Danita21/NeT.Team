# PREGUNTAS ADICIONALES

## 1. Teniendo en cuenta las características del ensamblador, ¿Cuál es la principal limitante que observan? Justifique su respuesta.

La principal limitante del ensamblador para la plataforma Hack radica en su naturaleza directa y la simplicidad del lenguaje simbólico que traduce. A diferencia de lenguajes de alto nivel, donde se pueden gestionar estructuras de datos complejas, abstracciones y operaciones sofisticadas, el ensamblador solo traduce instrucciones muy básicas (A-instrucciones y C-instrucciones) a código binario de 16 bits que la máquina Hack puede ejecutar directamente.
Justificación:
1. Simplicidad del Lenguaje Hack: El lenguaje ensamblador Hack es extremadamente sencillo, lo cual es útil para fines educativos, pero limita considerablemente la complejidad y el tipo de programas que se pueden escribir de manera eficiente. Cualquier tipo de abstracción debe ser manejada manualmente por el programador.
2. Resolución de Símbolos: Las etiquetas deben ser mapeadas a direcciones de memoria específicas, y la resolución de símbolos requiere múltiples pasadas sobre el código para garantizar que cada símbolo tenga un valor definido antes de ser utilizado en la traducción a binario.
3. Eficiencia: La falta de optimización es otra limitante. El ensamblador Hack traduce cada instrucción de manera bastante directa, sin aplicar optimizaciones que maximicen el uso del hardware.
4. Interactividad y Extensibilidad: El ensamblador no maneja multitarea ni características avanzadas como manejo de interrupciones.


# BONUS

## Inserte aqui la pregunta

Inserte aqui la respuesta.

# REFERENCIAS

https://www.nand2tetris.org/project06
