# Laboratorio de ADN

Este proyecto simula un laboratorio donde los usuarios pueden ingresar una cadena de ADN, detectar mutaciones, realizar mutaciones manualmente y sanar el ADN si está mutado.

## Participantes

- **Integrante 1**: Valentino Lorca
- **Integrante 2**: Luca Bertaina
- **Integrante 3**: Enzo Severino
- **Integrante 4**: Jeronimo Zuñiga

## Introducción de la cadena de ADN

Al ejecutar el programa, se pedirá que ingrese una cadena de ADN. La cadena debe cumplir con los siguientes requisitos:

- La cadena debe contener exactamente 6 partes, cada una con 6 bases nitrogenadas.
- Las bases nitrogenadas deben ser una combinación de **A**, **T**, **G** y **C**.
- Cada parte de la cadena debe estar separada por un espacio en blanco.
- La longitud total de la cadena (sin contar los espacios) debe ser de 36 caracteres.

### Ejemplo de una entrada válida:

GTACGT CTGATA AGGCAG GCATCG TGAGCG GCTACT

Si la cadena no cumple con estos requisitos, el programa solicitará que la ingreses nuevamente, indicando el error cometido (como caracteres no válidos o un número incorrecto de cadenas).

## Opciones disponibles

Después de ingresar una cadena de ADN válida, el programa te ofrecerá un menú de opciones para que puedas interactuar con la cadena de ADN. Las opciones disponibles son las siguientes:

1. **Detectar mutaciones**: Escribe "D" para verificar si existen mutaciones en la cadena de ADN. El programa te indicará si se detectó alguna mutación y el tipo de mutación encontrada.

   **Tipos de mutaciones posibles**:
   - **Radiación (Horizontal)**: Mutación detectada en una fila de la matriz de ADN.
   - **Radiación (Vertical)**: Mutación detectada en una columna de la matriz de ADN.
   - **Virus (Diagonal)**: Mutación detectada en una diagonal de la matriz de ADN.

   Si no se encuentra ninguna mutación, el programa te lo notificará.

2. **Mutar la cadena de ADN**: Escribe "M" para introducir mutaciones en la cadena de ADN. Tendrás la opción de elegir entre dos tipos de mutaciones:
   
   - **Virus (Diagonal)**: Ingresa las coordenadas de la fila y columna donde comenzará la mutación diagonal, así como la base nitrogenada que deseas repetir en la mutación.
   - **Radiación (Horizontal o Vertical)**: Elige entre una mutación horizontal o vertical, luego ingresa las coordenadas de la fila y columna para realizar la mutación. Después, elige una base nitrogenada que se repetirá en la mutación.

   Tras realizar la mutación, el programa te mostrará la nueva matriz de ADN con la mutación aplicada.

3. **Sanar la cadena de ADN**: Escribe "S" para sanar una cadena de ADN que ya ha sido mutada. El programa restaurará la cadena a su estado original.

4. **Salir**: Escribe "Q" para salir del programa.

Tras realizar cualquiera de estas opciones, el programa te ofrecerá nuevamente el menú para que puedas seguir interactuando con la cadena de ADN.
