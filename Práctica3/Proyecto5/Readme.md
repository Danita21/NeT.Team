# PRÁCTICA 3

## PROYECTO 5
### INTRODUCCIÓN
En los anteriores proyectos, se han contruido los componentes esenciales de procesamiento y almacenamiento de una computadora (la ALU y la RAM), ahora, el proyecto 5 de la página [nand2tetris](https://www.nand2tetris.org/project05) se basa en la creación de la plataforma de hardware Hack completa, implementando los componentes previamente hechos. El resultado será una compitadora de propósito general capaz de ejecutar programas escritos en el lenguaje de máquina Hack. 
En este proyecto se implementarán los siguientes chips:
- [CPU](#cpu)
- [Computer](#computer)
- [Memory](#memory)

### Códigos de los chips

#### CPU
El CPU es el componente encargado de ejecutar instrucciones y controlar el flujo de datos entre la memoria y el procesador, a continuación se explicará el funcionamiento del mismo:

##### Entradas y Salidas 
__Entradas:__ 
- __inM[16]:__ Es el valor de 16 bits que proviene de la memoria (M). 
- __instruction[16]:__ La instrucción de 16 bits que la CPU debe ejecutar.
- __reset:__ Señal qie indica si el programa debe reiniciarse (reset==1) o continuar desde donde se dejó(reset==0). 
__Salidas:__
- __outM[16]:__ Salida de 16 bits qie envía el valor de M que ha sido calculado por la ALU. 
- __writeM:__ Señal que indica si se debe escribir el valor en outM en la memoria M. 
- __addressM[15]:__ Dirección de memoria donde se guardará o se leerá el valor de M.
- __pc[15]:__ Dirección de la siguiente instrucción a ejecutar (Program Counter o PC).
##### Componentes internos
- __ALU:__ Es el bloque encargado de realizar operaciones aritm[eticas y l[ogicas. Toma dos entradas, outD y outAM (datos del registro D y A/M), y usa bits especificos de la instrucción para controlar la operación. Las señales zx, nx, zy, ny, f y no controlan las funciones de la ALU
  - zx, nx: Controlan si la entrada x (del registro D) se debe utilizar o negar.
  - zy, ny: Controlan si la entrada y (del registro A/M) se debe utilizar o negar.
  - f: Selecciona la operación de la ALU, aritmética (suma) o lógica (AND).
  - no: Indica si el resultado final debe ser negado.
  - Las salidas son outM (resultado de la ALU), zr (indica si el resultado es cero), y ng (indica si el resultado es negativo).
    
- __Registros:__ 
  - ARegister: El registro A guarda las direcciones de memoria. Su salida de conecta tanto a la direccion de memoria (addressM) como a la entrada de la ALU. Este registro se carga con loadA.
  - DRegister: El registro D almacena datos para operaciones aritméticas o lógicas. Se carga con outALU y su valor se envia a la ALU
  - PC (Program Counter): El contador de programa, que guarda la dirección de la próxima instrucción. Tiene señales para cargar nuevas direcciones, incrementar y reiniciar.  
- __Multiplexotes (MUX):__
  - El primer MUX selecciona entra la salida de la ALU o la instrucción para alimentar el registro A.
  - El segundo MUX selecciona entre el valor del registro A o la memoria M para ser enviado a la ALU como entrada y.
- __Decodificador de instrucciones:__ Esta lógica interpreta la intrucción y establece que hacer con los resultados de la ALU, se usan varios and, or y not para decidir como cargar los registros y manejar saltos condicionales. Esto permite a la CPU adaptarse a diferentes tipos de intrucciones, asegurando que cada operación se ejecute correctamente según la lógica de programacion definida.
- __Control de saltos y cargas:__
  - La lógica de salto decide si el contador de programa debe cambiar según las condiciones de la ALU y los bits de la instrucción.
  - La señal AMtoALU controla si la ALU debe usar la salida del registro A o el valor de la memoria.  
    
#### Computer
El chip Computer integra varios componentes para formar un sistema completo que pueda ejecutar programas:
##### Entradas
- __Reset:__ Esta entrada se utilizaa para reiniciar el sistema, permitiendo que el programa comience desde el principio si es necesario.
##### Componentes Internos
- __ROM32K:__
  - Este componente representa una memoria de solo lectura (ROM) con capacidad para almacenar hasta 32 kilobytes de instrucciones.
  - La entrada address determina cual instrucción se debe leer de la ROM, mientras que out proporciona la intrucción que se va a ejecutar.
  - La ROM se inicializa con el programa que la CPU ejecutará.
- __CPU:__
  - La CPU es el corazón del sistema, donde se lleva a cabo el procesamiento de las instrucciones.
  - Recibe como entradas inM, que proviene de la memoria, instruction, que es la instrucción leída de la ROM, y reset, que controla si la CPU debe reiniciarse.
  - Produce varias salidas como writeM, que indica si se debe escribir en lla memoria, outM, que es el resultado de la operación de la CPu, y pc, que señala la duireccion de la siguiente instrucción a ejecutar.
- __Memory:__
  - Este componente representa la memoria RAM del sistema, que es utilizada para almacenar y recuperar datos durante la ejecuci[on del programa.
  - La entrada in recibe el valor de outM proveniente de la CPU, load indica si se debe escribir en la memoria, y address determina en que dirección de la memoria se debe realizar la operación.
  - La salida out proporciona el contenido de la dirección de memoria solicitada, que se envía a la CPU como inM

#### Memory
Actua como un sistema que integra RAM, pantalla y teclado, gestiona la lectura y escritura de datos de la RAM y permite la comunicación con el dispositivo de pantalla y la entrada del teclado.  
##### Entradas y Salidas
__Entradas__
- __in[16]:__ Esta entrada de 16 bits es el valor que se desea escribir en la memoria.
- __load:__ Señal que indica si se debe cargar un nuevo valor en la memoria.
- __address[15]:__ Dirección de 15 bits que determina donde se realizará la lecutra o escritura en la memoria.
__Salida__
- __out[16]:__ Salida de 16 bits que porporciona el dato leído de la memoria
##### Componentes Internos
- __RAM16K:__ Este componente representa una memoria RAM de 16 kilobytes. La entrada in se utiliza para escribir datos en la RAM, mientras que load activa la escritura cuando se recibe una señal. Por otro lado, la entrada address[0..13] especificala dorección de memoria donde se guardarán los datos. La salida out proporciona el valor almacenado en la dirección especificada.
- __Screen:__ El componente screen gestiona la salida visual del sistema, permitiendo que los datos se escriban en la pantalla. Al igual que la RAM, recibe una entrada in para los valores que se desean mostrar, y la señal load indica cuando se debe actualizar la visualización. La dirección de salida address[0..12] determina qué parte de la pantalla se está actualizando. La salida out proporciona los datos visualizados en la pantalla.
- __Keyboard:__ El componente Keyboard es responsable de capturar la entrada del usuario desde el teclado. Este dispositivo convierte las pulsaciones de teclas en datos que el sistema puede procesar. La salida out proporciona el valor ingresado por el usuario, lo que permite que la CPU reciba y procese la información de manera efectiva.
- __DMux4Way:__ Es un demultiplexor que dirige la señal de carga a uno de los componentes internos según los bits de selección address[13..14]. Este componente recibe la señal de load y utiliza las direcciones de selección para activar una de las tres señales de carga: RAMLoadA, RAMLoadB o ScreenLoad. Gracias a su función, el DMux4Way asegura que la operación de carga se dirija correctamente al componente adecuado.
- __Or:__ El circuito Or combina las señales de carga provenientes de RAMLoadA y RAMLoadB, generando una única señal de carga (RAMLoad). Esta lógica es esencial para determinar si se debe realizar una operación de escritura en la RAM. Si al menos una de las señales de carga está activa, la salida de este circuito permitirá que los datos se almacenen en la RAM.
- __Mux4Way16:__ Es un multiplexor que selecciona entre las salidas de diferentes componentes internos: RamOut1, otra instancia de RamOut1, screenOut, y keyboardOut1. Utilizando los bits de selección address[13..14], este multiplexor dirige la salida a la línea general out. Esto permite que el sistema elija de manera eficiente qué dato proporcionar en función de la dirección de memoria, asegurando que la CPU tenga acceso a la información correcta en el momento adecuado y facilitando la interacción con múltiples dispositivos de entrada y salida.

### BIBLIOGRAFÍA  
Nisan, N., & Schocken, S. (n.d.). Nand2Tetris: The Elements of Computing Systems. Retrieved from https://www.nand2tetris.org/ 
