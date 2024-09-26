# PRÁCTICA 3
En esta práctica se realizaron los proyectos 4 de la página nand2tetris, los cuales consisten en programación de bajo nivel utilizando lenguaje ensamblador y la plataforma Hack.

## PROYECTO 4
### INTRODUCCIÓN
El proyecto 4 de la página nand2tetris se basa en familiarizarse con la programación en lenguaje ensamblador para la computadora Hack, comprendiendo el proceso de ensamblado y la ejecución del código binario en hardware. Se trabajará con dos programas en lenguaje ensamblador que permitirán experimentar de cerca con el lenguaje de máquina.

### PROGRAMAS
### Mult.asm
Este programa realiza una multiplicación entre los valores almacenados en los registros de la Hack RAM. Específicamente, multiplica los valores en R0 y R1, almacenando el resultado en R2. Los valores se encuentran en las primeras 16 posiciones de RAM (R0...R15).

#### Objetivo:
Calcular R0 * R1 y almacenar el resultado en R2.

#### Implementación:
El programa asume que R0 ≥ 0, R1 ≥ 0 y que R0 * R1 < 32768.
No es necesario validar estas condiciones en el código.
#### Procedimiento:
- Escribir el programa Mult.asm en un editor de texto utilizando el lenguaje ensamblador Hack.
- Ensamblar el archivo utilizando el ensamblador de Hack, generando el archivo Mult.hack con las instrucciones binarias.
- Cargar y ejecutar el archivo .hack en el emulador CPU.
- Utilizar el script Mult.tst para probar el programa y corregir errores de ser necesario.

### Fill.asm
Este programa maneja la entrada/salida del teclado y la pantalla de manera básica. El programa corre un bucle infinito que escucha la entrada del teclado. Cuando se presiona una tecla, el programa llenará la pantalla de color negro, y cuando no se presiona ninguna tecla, la pantalla se mantendrá en blanco.

#### Objetivo:
Escuchar la entrada del teclado y alternar entre una pantalla completamente negra y una pantalla completamente blanca dependiendo de si se presiona una tecla.

#### Implementación:
La pantalla se llena de negro cuando se detecta una tecla presionada.
La pantalla se limpia (se llena de blanco) cuando no se detecta ninguna tecla presionada.
La secuencia en la que se llenan los píxeles no es relevante, siempre que la pantalla se llene completamente de un color.

#### Procedimiento:
- Escribir el programa Fill.asm siguiendo las especificaciones anteriores.
- Probar el programa usando el emulador de CPU de Hack.
- Ejecutar el script Fill.tst y realizar pruebas interactivas para verificar su correcto funcionamiento.
- Utilizar el script FillAutomatic.tst para realizar pruebas automáticas con el archivo FillAutomatic.cmp que compara la salida esperada con la generada.

### CONCLUSIÓN
Estos dos programas permiten desarrollar un entendimiento profundo de la programación de bajo nivel, destacando la importancia de la traducción entre lenguajes de alto nivel y lenguaje de máquina


# REFERENCIAS
[1] Nisan, N., & Schocken, S. (n.d.). Nand2Tetris: The Elements of Computing Systems. Retrieved from https://www.nand2tetris.org

