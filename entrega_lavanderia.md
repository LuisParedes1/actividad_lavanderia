# Impresion

A primera vista, el problema tiene dificultad intermedia. La mayor dificultad que estoy teniendo es en la interpretacion del enunciado. 
El problema no parece largo. 

# Objetivo

Buscar que el tiempo de lavado sea el mínimo posible.

# Ideas a resolver

Leer de archivo, para cada prenda, sus incompatibles y el peso de la misma.

Ordenar segun su tiempo de lavado. 

La idea es agrupar todas las prendas que tengan el maximo tiempo de lavado juntas de manera que haya un unico lavado para estas. 

## Supuestos

- Si la prenda 1 es incompatible con la prenda 2, asumo que el reciproco es cierto (la prenda 2 es incompatible con la prenda 1)
- Una prenda se lava en un unico lavado y el tiempo de lavado es el de la prenda mas sucia.
- 

# ChangeLog

- Version 0: Se leyo del archivo las prendas y ordeno segun el tiempo de lavado y luego se fueron agregando sus compatibles.

    Para determinar los compatibles se utilizo teoria de conjuntos. Siendo X el conjunto de todas las prendas disponibles e Y el conjunto de incompatibles para una prenda, las prendas compatibles seran X-Y (la diferencia de conjuntos)

    Se van agregando las prendas compatibles en un lavado si estas son compatibles con las prendas existentes dentro del lavado.

- Version 1: Cambie el orden en que voy agregando las prendas compatibles. 
    Ahora ordeno segun el tiempo de lavado de manera que vaya agregando siempre las prendas compatibles mas pesadas (de mayor tiempo de lavado) en un principio


# Comentarios Finales

TO-DO
