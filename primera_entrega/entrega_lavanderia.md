# Impresion

A primera vista, el problema tiene dificultad intermedia. La mayor dificultad que estoy teniendo es en la interpretacion del enunciado. 
El problema no parece largo. 

# Objetivo

Buscar que el tiempo de lavado sea el mínimo posible.

# Ideas a resolver

Leer de archivo, para cada prenda, sus incompatibles y el peso de la misma.

Ordenar las prendas segun su tiempo de lavado. 

La idea es agrupar todas las prendas compatibles entre si que tengan el maximo tiempo de lavado juntas de manera que haya un unico lavado para estas. Se van agrupado en grupos que sean compatibles entre si y tomen el maximo tiempo de lavado posible. 

# ¿Como hacerlo?

Para agruparlos usare teoria de conjuntos. 
Por ejemplo, para obtener las prendas compatibles para la prenda 2, busco todas las prendas que no pertenezcan en el conjunto de prendas incompatibles para la misma haciendo una diferencia de conjuntos (TODAS_PRENDAS - INCOMPATIBLES) 

Luego voy agregando las prendas compatibles para un mismo lavado segun el orden de su tiempo de lavado.

Cuando se llegue a un conjunto de prendas compatibles se meten todas en un mismo lavado y el tiempo del mismo es el de la prenda de mayor tiempo.

Este proceso lo repito hasta que todas las prendas esten en un unico lavado.

## Supuestos

- Si la prenda 1 es incompatible con la prenda 2, asumo que el reciproco es cierto (la prenda 2 es incompatible con la prenda 1)
- Una prenda se lava en un unico lavado y el tiempo de lavado es el de la prenda mas sucia.
- No hay factores externos que alteren las contastes (por ejemplo: la lavadora se dañe, tome mas de un ciclo en lavarse, etc)

# ChangeLog

- Version 0: Se leyo del archivo las prendas y ordeno segun el tiempo de lavado y luego se fueron agregando sus compatibles.

    Para determinar los compatibles se utilizo teoria de conjuntos. Siendo X el conjunto de todas las prendas disponibles e Y el conjunto de incompatibles para una prenda, las prendas compatibles seran X-Y (la diferencia de conjuntos)

    Se van agregando las prendas compatibles en un lavado si estas son compatibles con las prendas existentes dentro del lavado.

- Version 1: Cambie el orden en que voy agregando las prendas compatibles. 
    Ahora ordeno segun el tiempo de lavado de manera que vaya agregando siempre las prendas compatibles mas pesadas (de mayor tiempo de lavado) en un principio

    El beneficio con este metodo es que se recorto el tiempo de lavado de 82 hasta 62

# Comentarios Finales

Se llego a que el minimo tiempo de lavado es de 62. 

La resolucion llegada del problema es bastante computacionalmente demandante y para una muestra mas grande puede ser ineficiente. Sin embargo el costo computacional o de tiempo de procesamiento no es un limitante para este problema asi que se toma como solucion valida del problema.