# PRÁCTICA 2
En esta práctica se realizaron los proyectos 2 y 3 de la página [nand2tetris](https://www.nand2tetris.org/) los cuales consisten en lógica aritmética y lógica secuancial respectivamente.

## PROYECTO 3
En este proyecto nos enfocamos en construir todos los chips descritos en el capitulo 3, hasta llegar a una unidad de memoria de acceso aleatorio.
    
### Códigos de los chips

### Bit

Para poder tener una unidad de persistencia de memoria de un bit tenemos que poder guardar y cargar informacion, para esto tenemos dos inputs in y load, este ultimo nos sirve como condicion para saber si debemos guardar nueva informacion o mantener la informacion anterior de forma que si el load es 1 ingresamos nueva informacion, de lo contrario mantenemos la informacion, para realizar esto utilizamos un multiplexor asignando el load al valor del selector para que el decida que informacion pasa, para las entradas hacemos un loop usando un data flip flop DFF cuya entrada es la salida del Mux y su salida vuelve al segundo input del Mux, de esta forma si el load carga un in = 1 el flip flop cargá la nueva entrada en cambio si el load no es 1 el flip flp cargará la informacion que tenia antes.

### Register

El register es un conjunto de x bits, en este caso es un registro de 16 bits, para su realizacion utilizamos el chip de bit que realizamos anterior mente, asignando un bit para cada uno de los 16 valores del input, pero le asignamos a todos los 16 bits el mismo valor del load, con el cual el registro sabra si debe almacenar la informacion en caso de que el load sea uno o no almacenar la informacion del input en caso que el load sea diferente a uno.

### RAM8

La RAM de 8 registros funciona tal y como su nombre lo indica con solo 8 registers. Lo primero que realizamos fue utilizar un demultiplexor para cargar el load a la direccion del registro utilizando el ADRESS al que se desea acceder, una vez hecho esto, todas las salidas del demultiplexor se cargan a la entrada load de cada register, de esta manera solo se actualiza el registro seleccionado. Para leer utilizamos un multiplexor cuyas entradas son las salidas de cada registro de manera que segun el adress, solo se mostrara la salida seleccionada. Asi obtuvimos una Ram de 8 registros que nos permite almacenar informacion y es la base para realizar las RAM compuestas.

### RAM64

Para realizar la RAM de 64 necesitamos 8 RAMs de 8 registros, por lo que la logica funciona de la misma manera, llegando a ser algo recursivo, y probablemente la causa de la demora en muchos de estos chips y posteriores. Al igual que con la RAM de 8 lo primero es un demultiplexor que en este caso no selecciona el registro sino la RAM 1,2,3...8, para esto nuestro adress ahora es de 6 bits y utilizamos los 3 mas significativos para seleccionar la RAM y los 3 menos significativos para seleccionar el registro dentro de esta RAM. Este demultiplexor asigna el load a la RAM8 correspondiente segun el adress[3..5] (bits mas significativos) y cada una de las RAM8 envia la salida del demultiplexor correspondiente. Pero dentro de las RAM8 enviamos como adress sus bits menos significativos adress[0..2]. Finalmente para leer usamos otra vez un multiplexor cuyas entradas con las salidas de cada RAM8 y solo permitira la salida de aquella que corresponda a la salida del adress[3..5].

### RAM512

Como se menciono en los apartados anteriores, el principal problema de utilizar tanta recursividad es que cada segundo se vuelve mas lento el programa en ejecucuion, ya que en este caso, una RAM512 invoca 8 RAM64, cada una de estas 8 RAM8 y cada una de estas 8 register sin mencionar sus bits. Al igual que las anteriores bits se utiliza un demultiplexor para escribir y selecciona la RAM64 con los 3 bits mas signifcativos adress[6..8] y llama las RAM64 enviandoles como adress[0..5]. Para leer se utiliza un multiplexor que recibe las salidas de las RAM64 y selecciona la salida con adress[6..8]. Podemos concluir a esta altura que los 3 bits mas significativos del adress se utilizan en los DMUX Y MUX, mientras que el resto de bits se envian a la funcion RAM interna.

### RAM4k

La RAM4K se compone de 8 RAM512 y un adress de 12 bits, al igual que en las anteriores, se usa un demultiplexor para asignar el load a la posicion de RAM correcta usando los 3 bits mas significativos del adress y se envian estos load o salidas del DMUX a cada una de los RAM512, las salidas de estas RAM512 entran a un multiplexor y segun adress[9..11] obtenemos la salida requerida.

### RAM16K

La RAM16K se compone de 8 RAM4K y un adress de 15 bits, al igual que en las anteriores, se usa un demultiplexor para asignar el load a la posicion de RAM correcta usando los 3 bits mas significativos del adress y se envian estos load o salidas del DMUX a cada una de los RAM4K, las salidas de estas RAM4K entran a un multiplexor y segun adress[12..14] obtenemos la salida requerida.

### PC

Para este counter requerimos informacion de la RAM a la cual llamamos outloop, y con ayuda de un add16 realizamos un incrementer, posteriormente con un multiplexor si la entrada inc es 1 guardamos el incremento, si no mantenemos la entrada procedente de la RAM. En un segundo MUX ingresamos la salida del anterior multiplexor t0 y la entrada in, si el load es 1 dejamos pasar la entrada in, de lo contrario mantenemos t0 en la salida llamada t1. Posteriormente en un multiplexor ingresamos t1 y false (equivalente a ceros), si reset es 1, la salida en t2 seran ceros, de lo contrario se conservara la entrada t1. Despues de esto, con ayuda de compuertas or miramos si hubo incremento, reset o load en el PC, es decir que una de estas entradas fuera 1, y en caso de serlo, registramos en la RAM t1.




