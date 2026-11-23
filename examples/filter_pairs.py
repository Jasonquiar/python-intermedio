"""Compara el filtrado de números pares con un bucle y con ``filter``."""

# =====================================================================
# CONCEPTO: filter()
# ---------------------------------------------------------------------
#   filter(función, iterable)
#
# Recorre el iterable y CONSERVA solo los elementos para los que
# la función devuelve True.
#
# Bases:
# - La función se pasa SIN paréntesis (is_pair, no is_pair()): se entrega
#   la función para que filter la llame por cada elemento.
# - Devuelve un ITERADOR (perezoso): se usa list() para ver los resultados.
# - Equivale a la comprensión:  [n for n in numbers if is_pair(n)]
# =====================================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = []

# El bucle conserva los números que cumplen la condición.
# % es el operador módulo (residuo): num % 2 == 0 significa "es par".
for num in numbers:
    if num % 2 == 0:
        pairs.append(num)

print(numbers)
print(pairs)


def is_pair(num: int)-> bool:
    """Indica si ``num`` es divisible por 2."""
    # Función "predicado": recibe un elemento y responde True o False.
    if num % 2 == 0:
        return True
    return False

# ``filter`` produce un iterador; ``list`` lo consume y guarda sus resultados.
pairs_filter = list(filter(is_pair, numbers))
print(pairs_filter)
