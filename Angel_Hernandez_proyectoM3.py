"""
Proyecto M3 - Simulación de la Máquina de Galton

Este programa simula una máquina de Galton con 3000 canicas y 12 niveles.
Cada canica se mueve aleatoriamente a la izquierda o a la derecha en cada nivel.
El contenedor final se calcula contando cuántas veces la canica se movió a la derecha.

Importante:
- No se usa la función normal().
- Se emplean dos funciones principales:
  1. calcular_contenedores()
  2. graficar_histograma()
"""

import random
import matplotlib.pyplot as plt


def calcular_contenedores(numero_canicas, niveles):
    """
    Calcula el contenedor final de cada canica.

    Parámetros:
    numero_canicas: cantidad total de canicas que se van a simular.
    niveles: cantidad de niveles de obstáculos de la máquina de Galton.

    Retorna:
    Una lista con el número de contenedor final de cada canica.
    El contenedor se representa con un número entre 0 y niveles.
    """
    resultados = []

    # Repetimos el proceso para cada canica de la simulación.
    for _ in range(numero_canicas):
        contenedor = 0

        # En cada nivel, la canica puede ir a la izquierda o a la derecha.
        for _ in range(niveles):
            movimiento = random.randint(0, 1)

            # Si el movimiento es 1, la canica se desplaza hacia la derecha.
            # Si el movimiento es 0, se queda en el mismo número de contenedor.
            if movimiento == 1:
                contenedor += 1

        # Guardamos el contenedor final donde cayó la canica.
        resultados.append(contenedor)

    return resultados


def graficar_histograma(resultados, niveles):
    """
    Genera un histograma con la distribución final de las canicas.

    Parámetros:
    resultados: lista con los contenedores finales de las canicas.
    niveles: cantidad de niveles de la máquina de Galton.
    """
    # Los bins se ajustan para que cada barra quede centrada en cada contenedor.
    bins = [i - 0.5 for i in range(niveles + 2)]

    plt.hist(resultados, bins=bins, edgecolor="black")

    # Título y nombres de los ejes solicitados en los criterios de evaluación.
    plt.title("Simulación de la Máquina de Galton")
    plt.xlabel("Contenedor final de la canica")
    plt.ylabel("Cantidad de canicas")

    # Mostramos todos los contenedores posibles, desde 0 hasta 12.
    plt.xticks(range(niveles + 1))

    # Mostramos el gráfico en pantalla.
    plt.show()


# Bloque principal del programa.
# Aquí se definen los valores solicitados en el documento del proyecto.
numero_canicas = 3000
niveles = 12

# Se calculan los contenedores finales de todas las canicas.
resultados = calcular_contenedores(numero_canicas, niveles)

# Se genera el histograma con los resultados de la simulación.
graficar_histograma(resultados, niveles)
