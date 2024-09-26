// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

(BEGIN)
    // Dirección para el valor de entrada del teclado.
    @24576
    D=A
    @keyboard
    M=D           // Guardar dirección de teclado en 'keyboard'.

(CHECK_KEYBOARD)
    // Dirección del último pixel en el mapa de la pantalla.
    @24575
    D=A
    @current
    M=D           // Guardar dirección del último pixel en 'current'.

    // Comprobar si se presionó una tecla.
    @keyboard
    A=M           // Apuntar a la dirección del teclado.
    D=M           // Cargar valor del teclado.
    @fillvalue
    M=-1          // Valor de llenado (-1) para la pantalla.
    @DRAW
    D;JNE         // Si una tecla está presionada (D != 0), salta a DRAW.

    // Si no se presionó ninguna tecla, limpiar la pantalla.
    @fillvalue
    M=0           // Valor de limpiado (0) para la pantalla.

(DRAW)
    // Llenar o limpiar el pixel actual dependiendo de 'fillvalue'.
    @fillvalue
    D=M           // Cargar valor de llenado o limpiado.
    @current
    A=M           // Apuntar a la dirección del pixel actual.
    M=D           // Asignar el valor al pixel.

    // Comprobar si ya se ha alcanzado el primer pixel del mapa.
    @current
    D=M           // Cargar la dirección actual del pixel.
    @16384
    D=D-A         // Restar la dirección base del primer pixel.
    @CHECK_KEYBOARD
    D;JLE         // Si ya se alcanzó el primer pixel, volver a 'CHECK_KEYBOARD'.

    // Decrementar la dirección del pixel actual.
    @current
    M=M-1         // Moverse al pixel anterior.
    
    // Continuar dibujando o limpiando el siguiente pixel.
    @DRAW
    0;JMP         // Saltar de nuevo a 'DRAW' para continuar el bucle.

