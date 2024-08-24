# Diferencia entre un IDE y un editor de texto

**IDE (Integrated Development Environment):**

Un IDE es un entorno de desarrollo integrado que proporciona un conjunto completo de herramientas para facilitar la programacion de software. Incluye un editor de codigo, un depurador, herramientas de compilacion e integracion con sistemas de control de versiones. Los IDEs suelen estar especializados en un conjunto particular de lenguajes de programacion y ofrecen caracteristicas como autocompletado de codigo, refactorizacion, y analisis de errores en tiempo real. Ejemplos de IDEs incluyen Visual Studio, Eclipse, IntelliJ IDEA, y PyCharm.

**Editor de texto:**

Un editor de texto es una herramienta mas basica que permite a los usuarios escribir y editar texto, incluido el codigo fuente. A diferencia de un IDE, los editores de texto no suelen incluir herramientas avanzadas como depuradores o compiladores. Sin embargo, muchos editores de texto modernos, como Visual Studio Code, Sublime Text, y Atom, pueden ampliarse con plugins para añadir funcionalidades adicionales, como soporte para diferentes lenguajes de programacion, control de versiones, y herramientas de linting.

**Diferencias clave:**

- Un IDE ofrece un conjunto completo de herramientas especificas para el desarrollo de software, mientras que un editor de texto se centra en la edicion de texto y puede ser ampliado con funcionalidades adicionales.
- Los IDEs suelen ser mas pesados en terminos de consumo de recursos y pueden ser mas complejos de configurar.
- Los editores de texto son mas ligeros y rapidos, pero pueden requerir configuracion adicional para proporcionar una experiencia de desarrollo similar a un IDE.

---

## Tipos de lenguajes de programacion (Tipados y no tipados)

**Lenguajes de programacion tipados:**

Un lenguaje de programacion tipado es aquel en el que cada variable y constante tiene un tipo de dato definido explicitamente. Esto significa que las operaciones sobre los datos deben ser compatibles con los tipos definidos. Existen dos categorias principales de tipado:

- **Tipado estatico:** Los tipos de las variables se definen en tiempo de compilacion y no pueden cambiar. Los errores de tipo se detectan antes de que el programa se ejecute. Ejemplos de lenguajes con tipado estatico incluyen Java, C++, y Rust.

- **Tipado dinamico:** Los tipos de las variables se determinan en tiempo de ejecucion. Esto permite mas flexibilidad, pero los errores de tipo solo se detectan durante la ejecucion del programa. Ejemplos de lenguajes con tipado dinamico incluyen Python, Ruby, y JavaScript.

**Lenguajes de programacion no tipados:**

Un lenguaje de programacion no tipado, o de tipado debil, es aquel en el que las variables no tienen un tipo de dato fijo. En estos lenguajes, es posible realizar operaciones entre diferentes tipos de datos sin necesidad de conversin explicita. Esto puede llevar a errores impredecibles si no se maneja adecuadamente. Ejemplos de lenguajes con tipado debil incluyen JavaScript y PHP.

---

## Tipos de datos en Java

**Numericos:**

Java proporciona varios tipos de datos numericos, tanto para enteros como para numeros de punto flotante:

- **byte**: Representa un entero de 8 bits con signo. Rango: -128 a 127.
- **short**: Representa un entero de 16 bits con signo. Rango: -32,768 a 32,767.
- **int**: Representa un entero de 32 bits con signo. Rango: -2^31 a 2^31 - 1.
- **long**: Representa un entero de 64 bits con signo. Rango: -2^63 a 2^63 - 1.
- **float**: Representa un numero de punto flotante de 32 bits.
- **double**: Representa un numero de punto flotante de 64 bits.

**Cadenas:**

- **String**: La clase `String` en Java se utiliza para representar cadenas de caracteres. Es un tipo de dato no primitivo y es inmutable, lo que significa que una vez que se crea una cadena, no se puede modificar.

**Fechas:**

Java utiliza la clase `Date` y las clases en el paquete `java.time` para representar y manipular fechas y tiempos.

- **Date**: Es una clase mas antigua que representa una fecha y una hora especificas. Su uso es menos recomendado en favor de las clases mas nuevas del paquete `java.time`.
- **LocalDate**: Representa una fecha sin hora (por ejemplo, 2024-08-23).
- **LocalTime**: Representa una hora sin fecha.
- **LocalDateTime**: Representa una combinacion de fecha y hora sin zona horaria.
- **ZonedDateTime**: Representa una fecha y hora con una zona horaria.
