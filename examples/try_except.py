"""Ejemplo de manejo de excepciones en Python."""

# =====================================================================
# CONCEPTO: Manejo de excepciones (try / except / finally) y raise
# ---------------------------------------------------------------------
#   try:      código que PUEDE fallar
#   except X: qué hacer si ocurre el error X (el programa no se detiene)
#   else:     (opcional) se ejecuta solo si NO hubo error
#   finally:  se ejecuta SIEMPRE, haya error o no (ej.: cerrar archivos)
#
# Bases:
# - Captura errores ESPECÍFICOS (ValueError, ZeroDivisionError...),
#   no un "except:" genérico que esconde todos los errores.
# - raise lanza un error a propósito.
# - Puedes crear tus propios errores heredando de Exception.
# =====================================================================


# Excepción personalizada: una clase que hereda de Exception.
class DivisionError(Exception):
    """Error personalizado para una operación de división no permitida."""

    # pass = "no agrego nada más"; hereda todo el comportamiento de Exception.
    pass


a = 0
b = 0

# Cada ``except`` maneja un error específico; ``finally`` se ejecuta al terminar.
try:
    # int("hola") lanza ValueError si el texto no es un número.
    a = int(input("Digita un número: "))
    b = int(input("Digita otro número: "))
    if b == 2:
        # raise: lanzamos nuestro propio error con un mensaje.
        # Ojo: ningún except de abajo lo captura, así que el programa se detiene
        # (después de ejecutar el finally).
        raise DivisionError("No está permitido el calculo por 2")
    # Si b == 0, Python lanza ZeroDivisionError automáticamente.
    resultado = a / b
    print(f"Resultado: {resultado}")
except ValueError:
    print("El valor que digitó no es un número válido")
except ZeroDivisionError:
    print("No está permitido dividir por 0")
finally:
    print("Print desde finally")

# Se llega aquí si el error fue capturado (o si no hubo error).
print("Este es otro print")
