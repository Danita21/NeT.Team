# PRÁCTICA 2
En esta práctica se realizaron los proyectos 2 y 3 de la página [nand2tetris](https://www.nand2tetris.org/) los cuales consisten en lógica aritmética y lógica secuancial respectivamente.

## PROYECTO 3

### INTRODUCCIÓN 

El Proyecto 3 de la página nand2tetris se centra en la implementación de la memoria de acceso aleatorio (RAM) y sus componentes básicos mediante el diseño y construcción de una serie de chips lógicos. Este proyecto es fundamental para entender la arquitectura de computadoras, ya que se basa en el diseño de unidades de almacenamiento y procesamiento básico, que son los bloques de construcción de sistemas computacionales complejos.

El objetivo principal de este proyecto es construir una memoria RAM de tamaño creciente, comenzando desde la unidad de almacenamiento más básica y escalando hasta una memoria de 16K. La práctica proporciona una visión profunda del funcionamiento interno de las memorias, que son esenciales para cualquier sistema informático.
    
### Códigos de los chips

### Bit

Un chip de bit es la unidad más básica de almacenamiento en memoria digital. Para implementar una unidad de persistencia de memoria de un bit, necesitamos mecanismos para almacenar y recuperar información. El chip de bit consta de dos entradas principales: in y load. La entrada load actúa como una señal de control para decidir si debemos almacenar nueva información o mantener la información anterior.

El funcionamiento se basa en un multiplexor (MUX) que selecciona entre la nueva información (in) y la información previamente almacenada en función del valor de load. Si load es 1, el MUX permite que la nueva entrada in sea almacenada. De lo contrario, mantiene la información anterior.

Para lograr esto, utilizamos un flip-flop D (DFF). La salida del MUX se conecta a la entrada del DFF, mientras que la salida del DFF se retroalimenta al segundo input del MUX. Así, si load es 1, el DFF actualiza su valor con la nueva entrada. Si load es 0, el DFF conserva su valor anterior.

El flip-flop D es fundamental en esta configuración porque garantiza que la información se retenga correctamente hasta que se decida actualizarla, asegurando estabilidad y consistencia en el almacenamiento de un bit.

### Register

Un register es un grupo de bits que se utiliza para almacenar datos temporales en un procesador o sistema de memoria. En el caso de un registro de 16 bits, se compone de 16 chips de bit conectados en paralelo. Cada bit en el registro opera de manera similar al chip de bit descrito anteriormente.

Cada uno de los 16 bits en el registro recibe el mismo valor para la señal load, lo que significa que todos los bits se actualizan simultáneamente cuando load es 1. Si load es 0, todos los bits mantienen su valor actual, garantizando que la información en el registro sea consistente y no se modifique accidentalmente.

Los registros son esenciales para operaciones de lectura y escritura rápidas en sistemas de computación, ya que permiten el almacenamiento temporal y el acceso a datos cruciales durante el procesamiento.

### RAM8

La RAM8 es una memoria de acceso aleatorio que consta de 8 registros de 16 bits cada uno. Para gestionar esta memoria, utilizamos un demultiplexor (DEMUX) para seleccionar qué registro (de los 8) se actualizará.

El DEMUX toma una dirección (ADDRESS) de 3 bits que indica cuál de los 8 registros debe ser seleccionado. La señal load se dirige solo al registro seleccionado, actualizando su contenido con la nueva información. Las demás salidas del DEMUX no afectan a los registros no seleccionados, preservando su información anterior.

Para la lectura, un multiplexor (MUX) selecciona la salida del registro basado en la misma dirección de 3 bits. Esto asegura que solo el registro seleccionado en la etapa de escritura sea el que se lea, proporcionando así la información correcta a la salida.

La RAM8 proporciona una estructura base para memorias más grandes y es fundamental en la jerarquía de almacenamiento de datos en sistemas digitales.

### RAM64

La RAM64 es una memoria de acceso aleatorio que se compone de 8 bloques de RAM8. La principal tarea aquí es seleccionar la RAM8 adecuada y el registro dentro de ella.

Se utiliza un DEMUX de 6 bits en esta RAM64. Los 3 bits más significativos del direccionamiento (ADDRESS) determinan cuál de las 8 RAM8 se debe activar para la operación de escritura. Los 3 bits menos significativos son utilizados para seleccionar el registro dentro de la RAM8 activa.

Dentro de cada RAM8, la señal load se dirige según los bits menos significativos del direccionamiento. Para la lectura, se emplea un MUX que selecciona la salida de la RAM8 correspondiente basada en los bits más significativos del direccionamiento. Esto permite acceder y gestionar 64 ubicaciones de memoria de manera eficiente.

### RAM512

La RAM512 amplía la capacidad de la RAM64 al incorporar 8 bloques de RAM64. Esta estructura jerárquica sigue un patrón recursivo similar al de RAM64 pero con una mayor capacidad de almacenamiento.

Un DEMUX de 9 bits gestiona la selección de las 8 RAM64. Los 3 bits más significativos del direccionamiento determinan cuál de las 8 RAM64 se activará, mientras que los 6 bits restantes se utilizan para seleccionar el registro dentro de la RAM64 activa.

Durante la lectura, un MUX selecciona entre las salidas de las 8 RAM64 basándose en los 3 bits más significativos del direccionamiento. Esta configuración permite gestionar hasta 512 ubicaciones de memoria, incrementando significativamente la capacidad de almacenamiento y recuperación de datos.

### RAM4k

La RAM4k se compone de 8 bloques de RAM512 y está diseñada para manejar 4,096 ubicaciones de memoria. Para gestionar esta cantidad, se utiliza un DEMUX de 12 bits.

En esta configuración, los 3 bits más significativos del direccionamiento seleccionan cuál de las 8 RAM512 se activará. Cada una de estas RAM512 recibe la dirección de 9 bits (los 9 bits menos significativos) para la selección del registro dentro de ellas.

Para la lectura, un MUX toma las salidas de las 8 RAM512 y selecciona la salida correspondiente basada en los bits más significativos del direccionamiento (ADDRESS[9..11]). Esto permite acceder a una gran cantidad de ubicaciones de memoria de forma eficiente.

### RAM16K

La RAM16K se expande aún más al incluir 8 bloques de RAM4k. La capacidad de almacenamiento de esta memoria es de 16,384 ubicaciones. Para manejar esta estructura, se utiliza un DEMUX de 15 bits.

En esta configuración, los 3 bits más significativos del direccionamiento determinan cuál de las 8 RAM4K se seleccionará para la escritura. Los 12 bits restantes se usan para seleccionar el registro dentro de la RAM4K activa.

El proceso de lectura utiliza un MUX que selecciona entre las salidas de las 8 RAM4K basándose en los 3 bits más significativos del direccionamiento (ADDRESS[12..14]). Esta jerarquía permite manejar grandes volúmenes de datos de manera eficiente y estructurada.

### PC

El Program Counter (PC) es un componente esencial en la arquitectura de computadoras que realiza un seguimiento de la dirección de la instrucción siguiente a ejecutar. Utiliza un add16 para incrementar la dirección actual en 1, facilitando la secuencia de ejecución de instrucciones.

La lógica del PC incluye varios MUX para gestionar la entrada de datos. Si inc es 1, el PC incrementa la dirección actual; si inc es 0, conserva la dirección de la RAM (outloop). Luego, un segundo MUX elige entre la dirección incrementada (t0) y una nueva entrada (in), dependiendo del valor de load.

Un tercer MUX se utiliza para manejar el reset. Si reset es 1, el PC se reinicia a cero; si no, conserva la dirección actual (t1). Finalmente, se utiliza una combinación de compuertas OR para verificar si ha habido un incremento, reset o carga, y actualizar el PC en consecuencia. Esto garantiza que el contador de programa mantenga la secuencia correcta y maneje adecuadamente las instrucciones del procesador.

#### BIBLIOGRAFÍA

Nisan, N., & Schocken, S. (n.d.). Nand2Tetris: The Elements of Computing Systems. Retrieved from https://www.nand2tetris.org/ 
