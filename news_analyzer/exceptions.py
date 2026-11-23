"""Definición de excepciones personalizadas para la aplicación."""


class NewsSystemError(Exception):
    """Clase base para los errores propios del sistema de noticias."""

    pass


class APIKeyError(NewsSystemError):
    """Error relacionado con la clave o la respuesta de una API."""

    pass
