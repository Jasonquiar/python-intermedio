"""Ejemplos de interpolación, expresiones y formatos con f-strings."""

# =====================================================================
# CONCEPTO: f-strings (formatted string literals)
# ---------------------------------------------------------------------
# Un string con una "f" delante permite insertar valores con {}.
#
#   f"texto {expresión}"
#   f"texto {expresión:formato}"
#
# Bases:
# - Dentro de {} va CUALQUIER expresión de Python: variables, cálculos,
#   llamadas a métodos o un if en una línea.
# - Después de ":" va el especificador de formato (decimales, ancho...).
# - Son la forma recomendada (más legible y rápida que .format() o %).
# =====================================================================

from datetime import datetime

name = "Ana"
year = 2020
# Interpolación básica: {name} se reemplaza por "Ana".
text = f"Hola {name}"
# Sin la "f" es un string normal: las {} se mostrarían tal cual.
text_2 = "Hola"

# ---------------------------------------------------------------------
# 1) EXPRESIONES dentro de las llaves
# ---------------------------------------------------------------------
# Una f-string puede evaluar una expresión al construir el texto.
text_calculo = f"Hola, {name}, tu edad es: {2025 - year} años"
print(text_calculo)

# También permite llamar métodos y usar expresiones condicionales.
text_func = f"HOLA {name.upper()}"
print(text_func)

edad = 16
# Operador ternario:  valor_si_true if condición else valor_si_false
# Se usan comillas simples adentro porque la f-string usa comillas dobles.
text_if = f"Hola {name}, eres {'mayor' if edad >= 18 else 'menor'} de edad"
print(text_if)


# ---------------------------------------------------------------------
# 2) ESPECIFICADORES DE FORMATO  {valor:formato}
# ---------------------------------------------------------------------
bank_balance = 1200000000
# Los especificadores después de ``:`` controlan cómo se presenta cada valor.
# :,    -> separador de miles  -> 1,200,000,000
text = f"Tu saldo en la cuenta bancaria es: {bank_balance:,}"

stock_price = 1.405
# :.1f  -> número decimal (f = float) con 1 decimal  -> 1.4
text = f"El valor del stock es: {stock_price:.1f}"

# :.2f  -> 2 decimales  -> 1.40 o 1.41 (los float no son exactos al redondear)
text = f"El valor del stock es: {stock_price:.2f}"

user_id = 10000
# :04d  -> entero (d) de mínimo 4 dígitos, rellenando con ceros a la izquierda.
#          5 -> "0005". Como 10000 ya tiene 5 dígitos, queda igual.
text = f"Su id es: {user_id:04d}"
print(text)


# ---------------------------------------------------------------------
# 3) ALINEACIÓN  < izquierda   > derecha   ^ centro
# ---------------------------------------------------------------------
product = "Laptop"
price = 1000

# :<15 -> ocupa 15 espacios alineado a la izquierda.
# :>10 -> ocupa 10 espacios alineado a la derecha. Sirve para hacer tablas.
text = f"Producto: {product:<15} | Precio: {price:>10}"
# \n es un salto de línea.
print(f"{text}\n{text}")


# ---------------------------------------------------------------------
# 4) FORMATO DE FECHAS (códigos de strftime)
# ---------------------------------------------------------------------
date = datetime(2024, 12, 5, 10, 10)
# %A día de la semana · %d día · %B mes · %Y año (4 dígitos)
# %I hora (formato 12 h) · %M minutos · %p AM/PM
# Nota: el espacio después de ":" también aparece en el resultado.
text = f"La fecha completa es {date: %A %d de %B de %Y a las %I:%M %p}"
print(text)
