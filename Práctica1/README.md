**Instalando y reconociendo las principales características de Nand2Tetris - Lógica Booleana**


**¿Qué es Nand2tetris?**

Nand2tetris es un curso creado por Noam Nisan y Shimon Schocken en conjunto con el libro The Elements of Computing Systems con el propósito de instruir a miles de personas de forma gratuita en la arquitectura de computadores. Por medio de un aprendizaje practico y teórico que abarca las diversas capas que conforma un sistema computacional actual.

**Introducción a la práctica:**

En este proyecto, nos enfocaremos en la construcción de un conjunto de compuertas lógicas fundamentales utilizando exclusivamente compuertas NAND primitivas. Este enfoque permite explorar y comprender cómo las compuertas NAND, que son una de las piezas clave en la lógica digital, pueden ser utilizadas para implementar una amplia variedad de funciones lógicas.
El objetivo es construir las siguientes compuertas: NOT, AND, OR, XOR, y multiplexores y demultiplexores de diversas configuraciones, incluyendo versiones de 16 bits y variantes más complejas como OR8Way y MUX8Way16. A través de este proyecto, no solo se implementarán estas compuertas, sino que también se obtendrá una comprensión profunda de cómo las compuertas NAND pueden ser combinadas para realizar funciones lógicas más avanzadas y versátiles.

**Objetivos:**

Construir todas las compuertas lógicas descritas en el Capítulo 1, lo que dará como resultado un conjunto de chips básico. Las únicas compuertas que puede utilizar en este proyecto son las puertas NAND primitivas y las compuertas compuestas que construimos gradualmente a partir de las NAND primitivas.

**Tipos de compuertas:**(Extraído directamente de The Elements of Computing Systems)

**NAND:** El punto de partida de nuestra arquitectura informática es la puerta Nand, a partir de la cual se construyen todas las demás puertas y chips. 

**Not:** La puerta Not de entrada única, también conocida como "convertidor", convierte su entrada de 0 a 1 y viceversa. And: La función And devuelve 1 cuando ambas entradas son 1 y 0 en caso contrario.

**Or:** La función Or devuelve 1 cuando al menos una de sus entradas es 1, y 0 en caso contrario. 

**Xor:** La función Xor, también conocida como “o exclusiva”, devuelve 1 cuando sus dos entradas tienen valores opuestos, y 0 en caso contrario.

**Multiplexor:** Un multiplexor es una compuerta de tres entradas que utiliza una de las entradas, llamada “bit de selección”, para seleccionar y generar una de las otras dos entradas, llamadas “bits de datos”. 

**Demultiplexor:** Un demultiplexor realiza la función opuesta de un multiplexor: toma una sola entrada y la canaliza a una de dos salidas posibles según un bit selector que especifica qué salida elegir. 

**Not multibit:** una compuerta Not de n bits aplica la operación booleana Not a cada uno de los bits en su bus de entrada de n bits.

**And multibit:** una compuerta And de n bits aplica la operación booleana And a cada uno de los n pares de bits dispuestos en sus dos buses de entrada de n bits .

**Or multibit:** una compuerta Or de n bits aplica la operación booleana Or a cada uno de los n pares de bits dispuestos en sus dos buses de entrada de n bits .

**Multiplexor multibit:** un multiplexor de n bits es exactamente igual al multiplexor binario, excepto que las dos entradas tienen n bits de ancho cada una; el selector es de un solo bit. 

**Or multidireccional:** una compuerta Or de n vías genera 1 cuando al menos una de sus n entradas de bit es 1, y 0 en caso contrario. Aquí está la variante de 8 vías de esta compuerta. 

**Multi-Way/Multi-Bit Multiplexor:** Un multiplexor de n bits de m vías selecciona uno de los m buses de entrada de n bits y lo envía a un solo bus de salida de n bits. La selección está especificada por un conjunto de k bits de control, donde k ¼ log2 m. 

**Multi-Way/Multi-Bit Demultiplexor:** Un demultiplexor de n bits de m vías canaliza una única entrada de n bits en una de las m posibles salidas de n bits. La selección está especificada por un conjunto de k bits de control, donde k ¼ log2 m.


**Descripción de los archivos**

**1.	Compuerta Not:** Para construir una compuerta NOT utilizando NAND, se puede usar una única compuerta NAND con ambas entradas conectadas a la misma señal de entrada. Esto da como resultado el complemento de la entrada. 

![image](https://github.com/user-attachments/assets/3f9e34ef-a92b-4458-8de6-f0fca46c4a1e)

 
**2.	Compuerta And:** Para implementarla usando compuertas NAND, primero se construye una compuerta NOT (como se describió anteriormente). Luego, se utiliza la compuerta NAND para generar la salida de AND y se niega su salida utilizando la compuerta NOT

![image](https://github.com/user-attachments/assets/d71642ad-6100-4147-9d96-631446a63837)

 
**3.	Compuerta Or:** Para construir una compuerta OR usando NAND, primero se construyen dos compuertas NOT, una para cada entrada. Luego, se utiliza una compuerta NAND para combinar las salidas de estas compuertas NOT

![image](https://github.com/user-attachments/assets/ff8cf4a1-7920-4dbf-80a7-ab25c1c425de)

 
**4.	Compuerta Xor:** Para implementarla con NAND, se utilizan varias compuertas NAND para combinar las entradas de forma que la salida sea 1 solo cuando las entradas son diferentes

![image](https://github.com/user-attachments/assets/0afb2b61-881d-4744-ba4f-762293aa9762)

 
**5.	Multiplexor (Mux):** Para construir un multiplexor de 2 entradas con NAND, se utilizan varias compuertas NAND para implementar la lógica de selección basada en las señales de selección.

![image](https://github.com/user-attachments/assets/07c1557f-68ff-4b7a-9e9e-5f83b372651e)

 
**6.	Demultiplexor (DMux):** Para implementar un demultiplexor con NAND, se utiliza una combinación de compuertas NAND para controlar la distribución de la entrada a las salidas.

![image](https://github.com/user-attachments/assets/03465e8a-f0cb-439b-962b-b60ec4bde606)

 
**7.	Compuerta Not16:** Se construye utilizando 16 compuertas NOT (como se describió anteriormente) aplicadas a cada bit de la entrada de 16 bits.

![image](https://github.com/user-attachments/assets/4d74c785-c0fe-4dca-a453-148e4a18c881)

 
**8.	Compuerta And16:** Se construye utilizando 16 compuertas AND de 1 bit (como se describió anteriormente), aplicadas a cada par de bits correspondientes de las dos palabras de 16 bits.

![image](https://github.com/user-attachments/assets/1c7ad287-4e81-4989-925f-3d8ff03951b6)

 
**9.	Compuerta Or16:** Se construye utilizando 16 compuertas OR de 1 bit (como se describió anteriormente), aplicadas a cada par de bits correspondientes de las dos palabras de 16 bits.

![image](https://github.com/user-attachments/assets/f53956b5-5200-41fc-a147-971225cc17ec)

 
**10.	Multiplexor16:** Se construye utilizando multiplexores de 1 bit para cada bit de la entrada de 16 bits, combinados de forma que la selección de una entrada de 16 bits se realiza de manera adecuada.

![image](https://github.com/user-attachments/assets/b846320e-014c-4194-b487-81f1125177b1)

 
**11.	Compuerta Or8Way:** Se construye utilizando multiplexores de 16 bits de 2 vías para combinar las 4 entradas en una salida seleccionada.

![image](https://github.com/user-attachments/assets/74b8350e-0c77-4b68-82b1-9b2ca7a0b7fd)

 
**12.	Multiplexor4Way16:** Se construye utilizando multiplexores de 16 bits de 2 vías para combinar las 4 entradas en una salida seleccionada.

**13.	Multiplexor8Way16:** Se construye utilizando multiplexores de 16 bits de 4 vías y 2 vías para combinar las 8 entradas en una salida seleccionada.

**14.	Demultiplexor4Way:** Se construye utilizando demultiplexores de 2 vías y combinaciones de compuertas NAND para controlar la distribución de la entrada a las 4 salidas.

**15.	Demultiplexor8Way:** Se construye utilizando demultiplexores de 4 vías y combinaciones de compuertas NAND para controlar la distribución de la entrada a las 8 salidas.


**Preguntas adicionales:**

¿Qué consideraciones importantes debe tener en cuenta para trabajar con Nand2Tetris?

Una de las consideraciones es familiarizarse con el simulador que ofrece el curso, ya que se usará para los ejercicios y circuitos. Es fundamental entender cómo probar y depurar los diseños dentro del simulador para garantizar su correcto funcionamiento.
Otra consideración es tener conocimientos previos sobre las compuertas lógicas, ya que se comienza construyendo todo a partir de puertas NAND. Además, es importante tener una mentalidad estructurada para ir resolviendo problemas paso a paso, ya que los proyectos se vuelven más complejos a medida que se avanza.

¿Qué otras herramientas similares a Nand2Tetris existen? (De mínimo dos ejemplos) 

Logisim: Un simulador gráfico que permite diseñar y probar circuitos lógicos, ideal para aprender sobre arquitectura de computadores y diseño de circuitos digitales.
CircuitVerse. Es una plataforma en línea que permite diseñar, simular y compartir circuitos lógicos de manera interactiva, con un enfoque educativo para aprender sobre electrónica digital y arquitectura de computadores.

**Referencias:**

Burch, C. (2003). Logisim: A graphical tool for designing and simulating logic circuits. Retrieved from https://sourceforge.net/projects/circuit/.

CircuitVerse Development Team. (n.d.). CircuitVerse Documentation. Retrieved from https://docs.circuitverse.org/.

Nisan, N., & Schocken, S. (n.d.). Nand2Tetris: The Elements of Computing Systems. Retrieved from https://www.nand2tetris.org/


