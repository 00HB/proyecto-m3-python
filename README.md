# Simulación de la Máquina de Galton

## Descripción del proyecto

Este proyecto consiste en simular una Máquina de Galton usando Python. La simulación utiliza 3000 canicas y 12 niveles de obstáculos.

En cada nivel, cada canica puede moverse aleatoriamente hacia la izquierda o hacia la derecha. Al final del recorrido, cada canica cae en un contenedor dependiendo de cuántas veces se movió hacia la derecha.

El objetivo del proyecto es observar cómo, aunque cada movimiento individual es aleatorio, la distribución final de las canicas tiende a concentrarse en los contenedores centrales, formando una figura parecida a una campana.

## ¿Cómo hice el programa?

Primero importé las librerías necesarias:

```python
import random
import matplotlib.pyplot as plt
```

La librería `random` se utilizó para generar números aleatorios y decidir si una canica se mueve hacia la izquierda o hacia la derecha.

La librería `matplotlib.pyplot` se utilizó para crear el histograma final con los resultados de la simulación.

El programa se divide en dos funciones principales:

## Función para calcular los contenedores

```python
calcular_contenedores()
```

Esta función simula el recorrido de las 3000 canicas.

Para cada canica, el programa repite 12 decisiones aleatorias, una por cada nivel de obstáculos. En cada decisión se genera un número aleatorio entre 0 y 1:

- Si sale 0, la canica se mueve hacia la izquierda.
- Si sale 1, la canica se mueve hacia la derecha.

El número total de veces que la canica se mueve hacia la derecha determina el contenedor final donde cae.

## Función para graficar el histograma

```python
graficar_histograma()
```

Esta función recibe la lista de resultados y genera un histograma usando `matplotlib`.

El histograma muestra cuántas canicas cayeron en cada contenedor. También incluye título y nombres en los ejes, como lo solicita la rúbrica del proyecto.

## Requisitos cumplidos

- Se simulan 3000 canicas.
- Se usan 12 niveles de obstáculos.
- Se utilizan números aleatorios.
- El programa tiene dos funciones.
- Una función calcula el contenedor final de cada canica.
- Una función genera el histograma.
- El histograma tiene título.
- El histograma tiene nombre en el eje X.
- El histograma tiene nombre en el eje Y.
- El código contiene comentarios explicando su funcionamiento.
- No se utiliza la función `normal()`.

## Resultado observado

Al ejecutar el programa, se genera un histograma donde la mayoría de las canicas caen en los contenedores centrales. Esto ocurre porque existen más combinaciones posibles de movimientos que llevan al centro que a los extremos.

Por ejemplo, para caer en un extremo, la canica tendría que moverse siempre hacia el mismo lado, lo cual es menos probable. En cambio, para caer en el centro, existen muchas combinaciones diferentes de movimientos hacia la izquierda y hacia la derecha.

## Reflexión

Este proyecto me ayudó a comprender mejor cómo se pueden usar los números aleatorios para simular procesos físicos. También reforcé el uso de funciones, ciclos `for`, condicionales y listas en Python.

Además, aprendí a representar datos mediante gráficas usando `matplotlib`, lo cual permite visualizar mejor los resultados de una simulación.

Durante el bootcamp he podido fortalecer mi lógica de programación y entender cómo dividir un problema en partes más pequeñas. Este proyecto fue útil porque combina varios temas importantes: funciones, estructuras de control, aleatoriedad y visualización de datos.
