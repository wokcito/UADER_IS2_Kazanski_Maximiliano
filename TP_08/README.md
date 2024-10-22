## Requerimientos

### Funcionales (R)

1. Solicita y acepta un número entero positivo
2. Valida que el número ingresado sea mayor a 0 y menor a 2000
3. Debe contar las iteraciones que se realicen hasta conseguir el valor 1
4. Si el número es par lo divide por 2
5. Si el número es impar lo multiplica por 3 y le suma 1
6. Si el número es 1 retorna la cantidad de iteraciones

### No funcionales (F)

## Test cases (T)

### Caja negra

1. Solicita un número
2. Valida que el número sea mayor a cero
3. Valida que el número sea menor o igual a 1999
4. Devuelve un integer (cantidad de iteraciones)
5. Si el número es 1 devuelve cero iteraciones
6. Si el número es 2 devuelve una iteración
7. Si el número es 3 devuelve siete iteraciones
8. Si el número es 1999 devuelve cincuenta iteraciones

### Caja blanca

9. Mientras el número no sea 1, si es par se divide por 2
10. Mientras el número no sea 1, si es impar se multiplica por 3 y se le suma 1
11. Si el número es 1 se retornan las iteraciones

## RTMX

| R - T | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|:-----:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:--:|:--:|
| 1     | x |   |   |   |   |   |   |   |   |    |    |
| 2     |   | x | x |   |   |   |   |   |   |    |    |
| 3     |   |   |   |   | x | x | x | x |   |    |    |
| 4     |   |   |   |   |   |   |   |   | x |    |    |
| 5     |   |   |   |   |   |   |   |   |   | x  |    |
| 6     |   |   |   | x |   |   |   |   |   |    | x  |

## Sesiones

1. Se encontró un defecto
2. Se encontraron tres defectos

## PCE y Densidad

Inspección: 1 / 4 = 0.25
Pruebas unitarias: 3 / 4 = 0.75
Pruebas funcionales: 0 / 4 = 0

Densidad de defectos: 4 / 18 = 0.2222

## TEP

Las siglas TEP significan Trabajo en Progreso (Work in progress), y tiene tiene un significado crítico ya que si aumentamos el trabajo en proceso, o sea las tareas que se estén realizando, pero no aumentamos el rendimiento, esto lleva a que plazo de ejecución se extienda. La idea entonces es bajar el TEP y aumentar el rendmiento, así el plazo de ejecución desciende.

![proyeccion](image.png)

## Marco para evaluar garantía en desarrollo de software

Mejorar el PCE en un proceso de calidad significa identificar y corregir más defectos en las etapas iniciales del ciclo de vida del software. Esto tiene varios beneficios para el tiempo total de pruebas y la garantía del software:

- Se reduce la cantidad de defectos que llegan a las fases finales, como las pruebas de aceptación o la producción.
- Disminuyen los tiempos de retrabajo, ya que es más fácil y económico solucionar los problemas en etapas tempranas.
- El ciclo de pruebas se vuelve más eficiente, lo que a su vez reduce costos y tiempos en el proyecto.

## 18

La organización tiene un PCE del 89% y libera 0.12 defectos por FP. Con un tamaño de proyecto de 100 FP, podemos evaluar lo siguiente:

a. Expectativa de defectos totales (µ0):
Si se liberan 0.12 defectos por FP, el total esperado de defectos sería:

b. Densidad de defectos al finalizar (δ0):
La densidad de defectos al finalizar la construcción se calcula como la proporción entre los defectos detectados y el tamaño del software en FP:

c. Defectos a planear durante V&V:
Dado que el PCE es del 89%, se estima que el 11% de los defectos (no detectados en las fases iniciales) serán encontrados durante V&V:
Defectos en V&V = media * 0.11 = 12 * 0.11 = 1.32 defectos

d. Opinión sobre los 60 defectos encontrados en los primeros 3 días de V&V:
Encontrar 60 defectos en los primeros días de V&V supera con creces lo que se esperaba (1.32 defectos). Esto sugiere que:
El PCE del 89% podría ser demasiado optimista.
Es probable que haya problemas significativos en las fases iniciales del desarrollo o en la detección de defectos, lo que indica la necesidad de revisar el proceso.

## 19

El artículo "Agile and software engineering" destaca que factores como la automatización de pruebas, la integración continua y el refactoring regular son fundamentales para mejorar la gestión de la deuda técnica. Esto se debe a que:

Automatización de pruebas: Permite un ciclo de retroalimentación más rápido, lo que reduce la probabilidad de introducir defectos en el código.

Integración continua: Facilita la identificación temprana de problemas de integración, evitando que la deuda técnica se acumule y se vuelva más difícil de manejar.

Refactoring regular: Contribuye a minimizar el impacto del código complejo o mal diseñado. Al abordar estos problemas de forma continua, se previene la generación de deuda técnica a largo plazo.

En conjunto, estos elementos mantienen el código en un estado más limpio y manejable, lo que, a su vez, disminuye los costos asociados a la deuda técnica en el futuro.

## 20

En el modelo simple de garantía, la implementación de una multa influye en el punto de equilibrio del proceso al incrementar el costo asociado a los defectos no detectados. Esto implica que:

Incremento en costos de defectos: Las multas hacen que los defectos sean más costosos para la organización, lo que lleva a una mayor inversión en actividades de prevención y detección de defectos. Así, se busca reducir la probabilidad de incurrir en sanciones.

Desplazamiento del punto de equilibrio: Debido a estos costos adicionales, el punto de equilibrio se moverá hacia un nivel de calidad superior. Es decir, se requiere un mayor esfuerzo para alcanzar y mantener estándares de calidad más altos para evitar las multas.
