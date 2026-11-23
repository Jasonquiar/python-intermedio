"""Módulo para interactuar con APIs de noticias."""

import json
import urllib
import urllib.parse
import urllib.request
from typing import Callable

from .config import BASE_URL
from .exceptions import APIKeyError


def validate_api_key(api_key: str) -> bool:
    """Valida que la API key tenga formato correcto.

    Args:
        api_key (str): La API key a validar.
    Returns:
        bool: True si la API key es válida, False en caso contrario.
    """
    return len(api_key) > 10 and api_key.isalnum()


def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    """Ejemplo de la interfaz de cliente para la API de The Guardian.

    Actualmente devuelve un texto de demostración; no realiza una solicitud HTTP.

    Args:
        api_key (str): La API key para autenticación.
        section (str): Sección de noticias a consultar.
        from_date (str): Fecha desde la cual obtener noticias (formato YYYY-MM-DD).
        timeout (int, optional): Tiempo máximo de espera usado por clientes HTTP.
        retries (int, optional): Parámetro de configuración común; aquí no se utiliza.

    Returns:
        str: Texto de demostración con la sección, fecha y timeout.
    """
    return f"Guardian {section} desde {from_date} con timeout {timeout}"


def newsapi_client(api_key, query, timeout=30, retries=3):
    """Consulta NewsAPI y decodifica la respuesta JSON.

    Args:
        api_key (str): La API key para autenticación.
        query (str): Término de búsqueda.
        timeout (int, optional): Tiempo máximo de espera de la solicitud.
        retries (int, optional): Parámetro de configuración común; aquí no se utiliza.

    Raises:
        APIKeyError: Si la respuesta HTTP produce un error HTTP.

    Returns:
        dict: Datos decodificados desde el JSON de la respuesta.
    """
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"
    try:
        # El bloque ``with`` asegura el cierre de la respuesta incluso si falla la lectura.
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.HTTPError:
        raise APIKeyError("Ocurrió un error, no se pudo conectar con la API")
    return f"NewsAPI: {query} con timeout {timeout}"


def fetch_news(api_name: str, *args: tuple, **kwargs: dict) -> dict:
    """Selecciona un cliente y le reenvía argumentos posicionales y nombrados.

    Args:
        api_name (str): Nombre del cliente: ``"newapi"`` o ``"guardian"``.
        *args: Argumentos posicionales que se reenvían al cliente seleccionado.
        **kwargs: Opciones nombradas que se combinan con la configuración base.

    Raises:
        ValueError: Si ``api_name`` no coincide con un cliente soportado.

    Returns:
        El valor que devuelva el cliente seleccionado.
    """

    if api_name not in ("newapi", "guardian"):
        raise ValueError(f"API '{api_name}' no soportada.")

    # La configuración recibida tiene prioridad sobre los valores predeterminados.
    base_config = {"timeout": 30, "retries": 3}
    config = {**base_config, **kwargs}
    api_clients: dict[str, Callable] = {
        "newapi": newsapi_client,
        "guardian": guardian_client,
    }
    client = api_clients[api_name]
    return client(*args, **config)
