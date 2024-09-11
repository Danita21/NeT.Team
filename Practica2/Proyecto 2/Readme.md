# PRÁCTICA 2
En esta práctica se realizaron los proyectos 2 y 3 de la página [nand2tetris](https://www.nand2tetris.org/) los cuales consisten en lógica aritmética y lógica secuancial respectivamente.
## PROYECTO 2
En el proyecto 2, denominado tambien como lógica aritmética, nos enfocamos en la contrucción de componentes funcamentales para el procesamiento aritmético dentro de la arquitectura de una computadora. La CPU y su núcleo ALU (Unidad Aritmético-lógica), son esenciales para realizar operaciones matemáticas y lógicas. En este proyecto se crearon una serie de chips claves como lo son: HalfAdder, FullAdder, Add16, Inc16 y culminando con la contruccion de un ALU para el ordenador Hack.    
### Códigos de los chips

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


