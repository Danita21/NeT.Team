# PRÁCTICA 2
En esta práctica se realizaron los proyectos 2 y 3 de la página [nand2tetris](https://www.nand2tetris.org/) los cuales consisten en lógica aritmética y lógica secuancial respectivamente.
## PROYECTO 2
### INTRODUCCIÓN

El proyecto 2 de la página nand2tetris se basa en implementar y comprender el chipset ALU (Unidad aritmético-Lógica) el cual es encargado de realizar cálculos escenciales, para ello se construirán los circuitos digitales que ejecutan operaciones aritméticas básicas en formato binario, los cuales son:  
- [HalfAdder](#halfadder)
- [FullAdder](#fulladder)
- [Add16](#add16)
- [Inc16](#inc16)
  
Finalmente, con estos chips se creará una [ALU](#alu) completa, proporcionando una comprensión práctica de la artmetica booleana y el diseño de circuitos, esenciales para la arquitectura de computadores.  

### CÓDIGOS DE LOS CHIPS  
#### HalfAdder
Este chip consiste en la suma de dos bits individuales. Siendo uno de los bloques básicos de construccion en circuitos aritméticos más complejos, como el **FullAdder** y la **ALU**. Su funcion principal es dumar dos bits y proporcionar dos resultados, la suma y el accarreo

El halfAdder tiene dos entradas:  
__a y b:__ que son los bits a sumar.  

y produce dos salidas:  
__sum:__ resultado de la suma de a y b.  
__carry:__ Acarreo a la siguiente posición.  

El halfAdder consta de dos puertas lógicas, XOR y AND
La puerta XOR calcula la suma, ya que da de salida 1 si y solo si un bit es 1.  
Por otro lado la puerta AND está encargada del acarreo, es decir, da 1 si hubo un acarreo hasta la siguiente posición en la Suma 

#### FullAdder
El fullAdder es un chip que extiende la funcionalidad del halfAdder. Mientras que el halfAdder suma dos bits y produce un acarreo, el fullAdder puede llegar a manejar tres bit entradas, dos bits a sumar y un accarreo de la posición anterior.

El fullAdder toma tres entradas:  
__a:__ primer bit a sumar.  
__b:__ segundo bit a sumar.  
__c:__ Acarreo de la posición anterior.  

Y produce dos salidas:  
__Sum:__ el bit resultante de la suma de a, b y c.  
__Carry:__ el acarreo a la siguiente posición  
El circuito del fullAdder esta compuesto por dos halfAdder y un Or

El primer halfAdder toma a y b para realizar la respectiva suma y carry
el segundo halfAdder toma el resultado de la suma anterior y 'c' para realizar la suma con el acarreo de la posicion anterior.
Para finalizar, el or toma los carry de los halfAdder's y determina si hay acarreo a la siguiente posición

#### Add16
Este chip realizaz la suma de dos numeros binarios de 16bits implementando los dos chips vistos anteriormente.

El chip Add16 toma dos entradas (a[16] y b[16) y produce una salida, igualmente de 16bits.  

El circuito de este chip esta construido con un halfAdder y 15 fullAdder, la razón de esto es que el halfAdder suma los bits menos significativos (a[0] y b[0) sin tener ningun acarreo de entrada, por otro lado, el acarreo final 'c16' indica si hubo un acarreo adicional luego de los 16 bits previos.

#### Inc16
El chip inc16 esta diseñado para aumentar en 1 un número binario de 16 bits. Este chip utiliza Add16 para realizar la operacion de incremento sumando 1 al número de entrada.  

Entradas:  
__in[16]:__ Un número binario de 16 bits.  
Salidas:  
__out[16]:__ El número binario incrementado en 1.  

El circuito del inc16 solamente contiene un add16. Para que el add16 sume solamente 1 al número ingresado, se determinan los siguientes parámetros:  
__b[0]=true:__ Con esto el chip add16 lee que el bit menos significativo de b sea 1.  
__b[1..15]=false:__ Los bits restantes de b estan configurados en 0, esto asegura que solamente se este sumando 1 al número previamente ingresado.  

#### ALU

el chip ALU (Unidad Aritmético-lógica) es un componente fundamental en la arquitectura de una computadora, encargado de realizar operaciones aritméticas y lógicas en dos números binarios de 16 bits. El diseño de este ALU permite realizar una variedad de operaciones en función de las señales de control proporcionadas.  

Entradas:

__x[16]__ y __y[16]:__ Los dos números de 16 bits para las operaciones.  
__ZX:__ Controla si la entrada 'x' debe ser 0.  
__nx:__ Controla si la entrada 'x' debe ser Negada.  
__zy:__ Controla si la entrada 'y' debe ser 0.  
__ny:__ Controla si la entrada 'y' debe ser Negada.  
__f:__ Controla si se debe realizar la suma (x + y) o la operacion AND (x & y).  
__no:__ Controla si la salida debe ser negada.  

Salidas:  

__out[16]:__ Resultado de la operacion aritmético-lógica.  
__zr:__ Señal que indica si la salida es cero.  
__ng:__ Señal que indica si la salida en Negativa.  

Detalles del diseño:  

##### Configuración de Entradas zx y zy
__Mux16:__ Se utiliza para selecciona entre la entrada original ('x' o 'y') y un valor de 0 (representado por 'false'). Esto se basa en los controles zx y zy.  

##### Negacion de entradas nx y ny
__Not16__ Se utiliza para negar las entradas seleccionadas por los multiplexores.  
__Mux16__ Luego, selecciona entre la entrada original y la negada basandose en los controles 'nx' y 'ny'.  

##### Operaciones aritméticas y lógicas f
Se realizan las operaciones de suma (Add16) y AND (and16).  
__Mux16__ selecciona el resultado de la suma o el resultado de la operacion AND seún el control 'f'

##### Negacion de salida no
__Not16__ niega la salida seleccionada.  
__Mux16__ permite seleccionar entre la salida original y la salida negada según el controlador 'no'  

##### Indicadores de Salida (zr y ng)
__zr:__ Se utiliza __Or8Way__ para verificar si la salida es cero. Se revisa cada byte (8 bits) de la salida para determinar si todos los bits son cero.
__ng:__ Se utiliza __And__ para verificar si el bit mas significativo (bit 15) de la salida es 1, lo que indica un número negativo.

### BIBLIOGRAFÍA  
Nisan, N., & Schocken, S. (n.d.). Nand2Tetris: The Elements of Computing Systems. Retrieved from https://www.nand2tetris.org/ 
