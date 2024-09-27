# PREGUNTAS ADICIONALES

## 1. ¿Por qué el lenguaje de máquina es importante para definir la arquitectura computacional?

El lenguaje de máquina es esencial para la definición de la arquitectura computacional porque actúa como el puente más directo entre el hardware y el software. La arquitectura computacional define el conjunto de instrucciones que la máquina puede ejecutar directamente, conocidas como el ISA (Instruction Set Architecture). Este conjunto de instrucciones es interpretado en forma de lenguaje de máquina, lo cual implica que cada operación realizada en un sistema, desde las aritméticas hasta el control de flujo, se codifica en binario, el formato que la CPU puede entender.

El lenguaje de máquina no solo dicta cómo interactúa el hardware con el software, sino que también establece las limitaciones y capacidades de un sistema en términos de rendimiento, eficiencia energética y escalabilidad. Dado que el hardware responde únicamente a este lenguaje, es fundamental para el diseño y la implementación de cualquier arquitectura computacional que los ingenieros diseñen un conjunto de instrucciones que maximice el uso de los recursos disponibles. Es decir, un diseño de arquitectura eficiente se basa en un lenguaje de máquina bien optimizado.

Además, los lenguajes de más alto nivel, como C o Python, se traducen eventualmente a lenguaje de máquina para ser ejecutados. Esta capa de traducción hace que el lenguaje de máquina actúe como una interfaz crucial que determina el rendimiento final de un programa.

## 2. ¿Qué diferencia ven entre arquitectura computacional, arquitectura de software y arquitectura del sistema? Justifique su respuesta.

La arquitectura computacional, la arquitectura de software y la arquitectura de sistema son conceptos diferentes que se centran en distintos aspectos del diseño y funcionamiento de un sistema de computación, aunque están interrelacionados.

### 1. Arquitectura computacional: 
Se refiere al diseño y la estructura interna de una computadora, específicamente cómo se organiza y opera el hardware para ejecutar instrucciones. Involucra el diseño del procesador (CPU), la memoria, el sistema de entrada/salida (E/S), el conjunto de instrucciones y la jerarquía de almacenamiento. Esta arquitectura se preocupa principalmente por cómo el hardware puede ejecutar eficientemente las instrucciones definidas en el ISA.

#### Ejemplo: 
La arquitectura x86 o ARM define cómo se comunican los componentes del hardware a través de instrucciones.

### 2. Arquitectura de software: 
Esta se centra en el diseño y la organización de los componentes de software de un sistema, y cómo estos interactúan entre sí. La arquitectura de software no se ocupa de cómo funciona el hardware, sino de cómo las diferentes partes del software están estructuradas, como los módulos, componentes, y subsistemas, y cómo se comunican mediante protocolos o APIs.

#### Ejemplo: 
Un patrón de arquitectura como el Modelo-Vista-Controlador (MVC) en desarrollo web.

### 3. Arquitectura de sistema: 
Es un término más amplio que abarca tanto el hardware como el software, describiendo cómo ambos interactúan para proporcionar las funcionalidades requeridas por el usuario. La arquitectura de sistema involucra todos los niveles, desde los dispositivos físicos hasta los componentes de software, y asegura que todos estos trabajen de manera coordinada para lograr los objetivos del sistema.

#### Ejemplo: 
La arquitectura de un sistema embebido que incluye la interacción entre sensores (hardware), el sistema operativo (software) y el middleware.

Pare terminar, la arquitectura computacional se centra en el hardware y cómo este ejecuta instrucciones; la arquitectura de software se enfoca en cómo está organizado el software para facilitar la interacción entre sus componentes; mientras que la arquitectura del sistema abarca ambos aspectos, asegurando una coordinación efectiva entre hardware y software.

# BONUS

## Como informático o computista: ¿La arquitectura computacional o la arquitectura del sistema no tiene en cuenta igualmente la arquitectura del software? Justifique su respuesta.

Desde una perspectiva informática, la arquitectura computacional y la arquitectura de sistema ciertamente consideran la arquitectura del software, pero no necesariamente la incluyen de manera explícita en su diseño. Esto se debe a que estas arquitecturas se centran en aspectos diferentes, pero interdependientes del diseño del sistema.

### Arquitectura computacional: 
Aunque está fundamentalmente orientada al diseño del hardware, no puede ignorar completamente el software, ya que la forma en que el software interactúa con el hardware influye directamente en la eficiencia y el rendimiento del sistema. Por ejemplo, las arquitecturas modernas como ARM y x86 están diseñadas teniendo en cuenta la optimización del código que se ejecuta en estos procesadores. Sin embargo, la arquitectura computacional no define explícitamente cómo debe estructurarse el software, sino que provee un marco eficiente para que el software lo utilice.

Un ejemplo claro de esta interdependencia es el uso de optimizaciones basadas en el hardware. Los compiladores de software a menudo están diseñados para generar código que aproveche características específicas de la arquitectura de hardware, como el paralelismo o las instrucciones SIMD (Single Instruction, Multiple Data). Sin embargo, la arquitectura computacional no dicta la organización interna de dicho software, que sigue siendo parte del dominio de la arquitectura de software.

### Arquitectura de sistema: 
En este caso, la interacción entre hardware y software es mucho más explícita. La arquitectura de sistema debe tener en cuenta la estructura del software para garantizar que el hardware y el software trabajen en armonía. Por ejemplo, en un sistema operativo, la arquitectura de sistema asegura que el software pueda manejar la administración de memoria, el control de procesos y la comunicación entre dispositivos de hardware de manera eficiente.

Aunque la arquitectura de sistema considera el software más directamente que la arquitectura computacional, sigue habiendo una distinción entre cómo se organiza el software internamente (arquitectura de software) y cómo se integra con el hardware.

En conclusión, la arquitectura computacional y la arquitectura de sistema tienen en cuenta el software en términos de su funcionamiento y optimización con respecto al hardware, pero no se preocupan por su estructura interna. Estas arquitecturas proporcionan el marco en el que el software debe funcionar, mientras que la organización y diseño del software quedan en el ámbito de la arquitectura de software.


# REFERENCIAS

Para pregunta 1:

Tanenbaum, A. S., & Austin, T. (2012). Structured Computer Organization. Pearson Education.

Patterson, D. A., & Hennessy, J. L. (2013). Computer Organization and Design: The Hardware/Software Interface. Morgan Kaufmann Publishers.

Para pregunta 2:

Bass, L., Clements, P., & Kazman, R. (2012). Software Architecture in Practice. Addison-Wesley Professional.

Stallings, W. (2015). Computer Organization and Architecture. Pearson Education.

Shaw, M., & Garlan, D. (1996). Software Architecture: Perspectives on an Emerging Discipline. Prentice Hall.

Para pregunta bonus:

Hennessy, J. L., & Patterson, D. A. (2017). Computer Architecture: A Quantitative Approach. Morgan Kaufmann.

Sommerville, I. (2010). Software Engineering. Addison-Wesley.

Gorton, I. (2011). Essential Software Architecture. Springer.

