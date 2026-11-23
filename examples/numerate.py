"""Ejemplos de recorridos con contador y con la función ``enumerate``."""

# =====================================================================
# CONCEPTO: enumerate()
# ---------------------------------------------------------------------
#   enumerate(iterable, start=0)
#
# Entrega pares (índice, elemento) mientras recorres una colección.
#
# Bases:
# - Evita crear y aumentar un contador a mano.
# - start define desde qué número se cuenta (por defecto 0).
# - Se usa con "desempaquetado":  for indice, elemento in enumerate(...)
# =====================================================================

from sample_data import sample_articles

# Este patrón mantiene el contador manualmente.
# Problema: es fácil olvidar el "counter = counter + 1".
counter = 1
for article in sample_articles:
    print(f'{counter}: {article}')
    counter = counter + 1

# ``enumerate`` entrega pares (índice, elemento); ``start`` define el índice inicial.
# Con start=10 el primer artículo sale con el número 10.
sample_articles_enum = enumerate(sample_articles, start=10)
# Desempaquetado: cada par (10, artículo) se reparte en counter y article.
for counter, article in sample_articles_enum:
    print(f'{counter}: {article}')
