"""Compara el cálculo de cuadrados con un bucle y con ``map``."""

# =====================================================================
# CONCEPTO: map()
# ---------------------------------------------------------------------
#   map(función, iterable)
#
# Aplica la función a CADA elemento y devuelve los resultados
# TRANSFORMADOS. Siempre devuelve la misma cantidad de elementos.
#
# Bases:
# - map TRANSFORMA (cambia cada elemento); filter SELECCIONA (descarta).
# - La función se pasa sin paréntesis.
# - Devuelve un ITERADOR: se usa list() para materializarlo.
# - Equivale a la comprensión:  [cuadraro(n) for n in numeros]
# =====================================================================

numeros = [1, 2, 3, 4, 5]
cuadrados = []

# En el bucle, cada resultado se agrega explícitamente a la lista.
# ** es el operador potencia: num ** 2 = num al cuadrado.
for num in numeros:
    cuadrados.append(num ** 2)


print(numeros)
print(cuadrados)

def cuadraro(num):
    """Devuelve el cuadrado de un número."""
    return num ** 2

# ``map`` aplica la función a cada elemento; ``list`` materializa el iterador.
# [1, 2, 3, 4, 5] -> [1, 4, 9, 16, 25]
cuadrados_map = list(map(cuadraro, numeros))
print(cuadrados_map)
