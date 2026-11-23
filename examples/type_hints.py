"""Explicaciones y ejemplos de type hints en Python."""

# =====================================================================
# CONCEPTO: Type hints (anotaciones de tipo)
# ---------------------------------------------------------------------
#   variable: tipo = valor
#   def funcion(param: tipo) -> tipo_de_retorno:
#
# Bases:
# - Python es de TIPADO DINÁMICO: una variable puede cambiar de tipo.
# - Los type hints son solo DOCUMENTACIÓN/AYUDA: Python NO los valida
#   al ejecutar. Los revisan el editor (VS Code) y herramientas como mypy.
# - Ventajas: autocompletado, detectar errores antes de ejecutar y
#   código más fácil de entender.
# =====================================================================

# Tipado dinámico: la misma variable pasa de int a str sin error.
variable = 42  # int
print(f"Variable: {variable}, del tipo: {type(variable)}")

variable = "Texto de prueba"
print(f"Variable: {variable}, del tipo: {type(variable)}")

# Con anotación decimos que "otra_variable" DEBERÍA ser int.
otra_variable: int = 44
print(f"Variable: {otra_variable}, del tipo: {type(otra_variable)}")

# Python lo permite igual (no valida), pero el editor marcaría la advertencia.
otra_variable = ""

# "int | None": puede ser un entero o None (útil para valores opcionales).
user_id: int | None = None

# variable = valor
# variable: tipo = valor


# Anotación de función: tipo de cada parámetro y "-> int" para el retorno.
def suma_clara(a: int, b: int) -> int:
    """Suma dos enteros; las anotaciones documentan tipos, no validan en ejecución."""
    return a + b


# Los tipos genéricos describen el contenido de colecciones anidadas.
# list[dict] -> una lista cuyos elementos son diccionarios.
articles: list[dict] = [
    {"title": "Example"},
    {"title": "Example 2"},
]

# list[list[str]] -> una lista de listas de strings.
articles_dos: list[list[str]] = [
    ["articulos", "otros"],
    ["articulos", "otros"],
]

# Any se importa del módulo typing (lo ideal es tener los imports arriba).
from typing import Any

# ``Any`` sirve cuando un elemento puede tener distintos tipos, pero reduce la precisión.
articles_tres: list[list[Any]] = [
    ["articulos", "otros", 123],
    ["articulos", "otros"],
]

# Tipos más usados: int, str, float, bool, list, dict, tuple, set, Any, None
