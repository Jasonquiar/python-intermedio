"""Ejemplos y explicaciones de comprehensions en Python."""

# =====================================================================
# CONCEPTO: Comprehensions (comprensiones)
# ---------------------------------------------------------------------
# Forma corta de CREAR una colección a partir de otra, en una expresión.
#
#   Lista:       [expresión for elemento in iterable if condición]
#   Diccionario: {clave: valor for elemento in iterable if condición}
#   Conjunto:    {expresión for elemento in iterable if condición}
#
# Bases:
# 1. expresión -> lo que se guarda (va PRIMERO).
# 2. for ... in -> el recorrido, igual que un bucle for normal.
# 3. if         -> filtro OPCIONAL; solo entran los que cumplen.
# - El tipo de paréntesis define el resultado: [] lista, {} dict/set.
# - Úsalas cuando la lógica es simple; si se vuelve difícil de leer,
#   es mejor un bucle tradicional.
# =====================================================================

from sample_data import sample_articles


# ---------------------------------------------------------------------
# 1) LIST COMPREHENSION
# ---------------------------------------------------------------------
def extract_titles_traditional(articles):
    """Devuelve los títulos de artículos cuyo título supera los 200 caracteres."""
    # Versión tradicional: 1) lista vacía, 2) recorrer, 3) filtrar, 4) append.
    titles = []
    for article in articles:
        if len(article["title"]) > 200:
            titles.append(article["title"])
    return titles


def extract_titles(articles):
    """Aplica el mismo filtro que ``extract_titles_traditional`` con una comprensión."""
    # La expresión va primero; después se indica el recorrido y, al final, el filtro.
    #   expresión -> article["title"]
    #   recorrido -> for article in articles
    #   filtro    -> if len(article["title"]) > 200
    # No hace falta crear la lista vacía ni llamar a append().
    return [article["title"] for article in articles if len(article["title"]) > 200]


# ---------------------------------------------------------------------
# 2) DICT COMPREHENSION
# ---------------------------------------------------------------------
def extract_article_summaries(articles):
    """Crea un diccionario título-descripción para descripciones de más de 5 caracteres."""
    # Lleva llaves {} y la expresión tiene la forma  clave: valor
    #   clave -> article["title"]    valor -> article["description"]
    return {
        article["title"]: article["description"]
        for article in articles
        if len(article["description"]) > 5
    }


print(extract_titles_traditional(sample_articles))
print("======")
print(extract_titles(sample_articles))
print(extract_article_summaries(sample_articles))


# ---------------------------------------------------------------------
# 3) SET COMPREHENSION
# ---------------------------------------------------------------------
# Un set (conjunto) NO permite elementos repetidos: ideal para valores únicos.
def get_sources_traditional(articles):
    """Obtiene los nombres de fuentes no vacíos y elimina duplicados con un conjunto."""
    # set() crea un conjunto vacío ({} crearía un diccionario vacío).
    sources = set()
    for article in articles:
        # .get() devuelve None en vez de lanzar KeyError si la clave no existe.
        if article.get("source") and article.get("source").get("name"):
            sources.add(article.get("source").get("name"))
    return sources


def get_sources(articles):
    """Obtiene las fuentes con una comprensión de conjunto."""
    # Llaves {} SIN "clave: valor" -> se crea un set, no un dict.
    # "TechNews" aparece 2 veces en los datos, pero el set lo guarda una sola vez.
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }


# ---------------------------------------------------------------------
# 4) COMPREHENSION ANIDADA (una comprensión dentro de otra)
# ---------------------------------------------------------------------
def categorize_traditional(articles):
    """Agrupa los artículos por fuente mediante bucles tradicionales."""
    sources = get_sources(articles)
    results = {}

    # Bucle externo: una clave por cada fuente.
    for source in sources:
        if source not in results:
            results[source] = []

        # Bucle interno: busca los artículos que pertenecen a esa fuente.
        for article in articles:
            if source == article.get("source").get("name"):
                results[source].append(article)

    return results


def categorize(articles):
    """Agrupa los artículos por fuente con una comprensión de diccionario anidada."""
    sources = get_sources(articles)
    # Por fuera: dict comprehension  -> {source: ... for source in sources}
    # Por dentro: list comprehension -> la lista de artículos de esa fuente.
    # Resultado: {"TechNews": [artículo1, artículo3], "Finance": [...], ...}
    return {
        source: [
            article
            for article in articles
            if source == article.get("source").get("name")
        ]
        for source in sources
    }


print(categorize_traditional(sample_articles))
print("===")
print(categorize(sample_articles))
