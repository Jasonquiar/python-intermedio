"""Ejemplos de argumentos variables con ``*args`` y ``**kwargs``."""

# =====================================================================
# CONCEPTO: *args y **kwargs (argumentos variables)
# ---------------------------------------------------------------------
# Permiten que una función reciba una cantidad VARIABLE de argumentos.
#
# *args    -> junta los argumentos POSICIONALES extra en una TUPLA.
# **kwargs -> junta los argumentos CON NOMBRE (clave=valor) en un DICT.
#
# Bases:
# - Lo importante es el * o el **; "args" y "kwargs" son solo convención.
# - Orden obligatorio en la firma:
#       def f(normales, *args, con_default=1, **kwargs)
# - Útil cuando no sabes cuántos parámetros llegarán (ej.: distintas APIs).
# =====================================================================


def ejemplo_args(api_key, *args):
    """Muestra cómo ``*args`` reúne argumentos posicionales en una tupla."""
    # api_key recibe el PRIMER argumento; todo lo demás cae en args.
    print(f"api_key: {api_key}")
    print(f"args: {args}")
    # type(args) -> <class 'tuple'>: es inmutable, no se puede modificar.
    print(f"type args: {type(args)}")
    print("====")


# Los valores posteriores a ``api_key`` se agrupan automáticamente en ``args``.
# Aquí args = ("Este", "parametro", "acá")
ejemplo_args("API_KEY_VALUE", "Este", "parametro", "acá")
# Aquí args = ("Hola", "Mundo"): la misma función acepta otra cantidad.
ejemplo_args("API_KEY_VALUE", "Hola", "Mundo")


def ejemplo_kwargs(**kwargs):
    """Muestra cómo ``**kwargs`` reúne argumentos con nombre en un diccionario."""
    # type(kwargs) -> <class 'dict'>: el nombre del argumento es la clave.
    print(f"kwargs: {type(kwargs)}")
    print(f"kwargs: {kwargs}")
    print("======")


# Los argumentos con nombre pueden variar entre llamadas sin cambiar la firma.
# kwargs = {"api_key": "DEMO", "query": "...", "timeout": 30, "retries": 3}
ejemplo_kwargs(
    api_key="DEMO",
    query="Noticias de Python",
    timeout=30,
    retries=3,
)
# Otra API con parámetros distintos (section, from_date): la función no cambia.
ejemplo_kwargs(
    api_key="DEMO_GUARDIAN",
    section="Sports",
    from_date="2020-10-20",
    timeout=30,
    retries=3,
)
