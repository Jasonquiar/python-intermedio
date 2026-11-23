"""Utilidades varias para la aplicación."""


def clean_text(text: str) -> str:
    """Quita espacios al inicio y al final y convierte el texto a minúsculas.

    Args:
        text (str): Cadena que se desea normalizar.

    Returns:
        str: Texto normalizado; si la entrada es vacía, devuelve una cadena vacía.

    Examples:
        >>> clean_text("  HOLA MUNDO  ")
        'hola mundo'

        >>> clean_text("Python Programming")
        'python programming'

        >>> clean_text("")
        ''

        >>> clean_text("MiXeD cAsE tExT   ")
        'mixed case text'
    """
    if not text:
        return ""
    return text.strip().lower()


def process_article_data(raw_data: dict) -> dict:
    """Reserva el punto de entrada para procesar un artículo.

    La implementación actual es un marcador de posición y devuelve un diccionario vacío.

    Args:
        raw_data (dict): Datos originales del artículo.

    Returns:
        dict: Diccionario vacío mientras no se implemente el procesamiento.
    """
    return {}


def get_unique_sources(articles):
    """Devuelve los nombres de fuentes presentes, sin duplicados ni valores vacíos."""
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }


def get_articles_by_source(articles: list[dict], source: str) -> list[dict]:
    """Filtra artículos por nombre de fuente sin distinguir mayúsculas."""
    return list(
        filter(
            lambda article: article["source"]["name"].lower() == source.lower(),
            articles,
        )
    )


def get_reading_time(article: dict) -> dict:
    """Agrega el tiempo estimado de lectura al artículo y devuelve el mismo diccionario.

    La estimación usa bloques enteros de 200 caracteres y suma un minuto.
    Esta función modifica ``article`` directamente.
    """
    minutes = len(article["content"]) // 200 + 1
    article["reading_time"] = minutes
    return article