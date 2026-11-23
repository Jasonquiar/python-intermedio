"""
Explicación de docstrings.

En esta clase puedo explicar cómo funcionan los docstrings en Python.
"""

# =====================================================================
# CONCEPTO: Docstrings vs comentarios
# ---------------------------------------------------------------------
# Docstring ("""..."""):
# - Es el PRIMER string dentro de un módulo, función o clase.
# - Python lo GUARDA en el atributo __doc__ del objeto.
# - Lo leen help(), VS Code (al pasar el mouse) y los generadores de docs.
# - Explica QUÉ hace y CÓMO se usa (parámetros, retorno).
#
# Comentario (#):
# - Python lo IGNORA por completo al ejecutar.
# - Explica el CÓMO o el PORQUÉ del código, para quien lo lee.
#
# Bases (PEP 257):
# - Usar siempre triples comillas dobles """.
# - Primera línea: resumen corto que termina en punto.
# - Si hay más detalle: línea en blanco y luego la explicación.
# =====================================================================


# Este ejemplo no tiene docstring para contrastarlo con la función siguiente.
def ejemplo_sin_docstring():
    return "Hola, mundo!"


def ejemplo_con_docstring() -> str:
    """Devuelve un saludo.

    Returns:
        str: El texto ``"Hola, mundo!"``.
    """
    # Formato "Google style": secciones Args:, Returns:, Raises: con sangría.
    return "Hola, mundo!"


# ``help`` muestra el docstring; ``__doc__`` permite acceder a él directamente.
print(ejemplo_con_docstring.__doc__)
help(ejemplo_con_docstring)
# Sin docstring, __doc__ vale None.
print(ejemplo_sin_docstring.__doc__)
