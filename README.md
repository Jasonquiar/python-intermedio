# 📰 News Analyzer · Python Intermedio
 
Mi copia comentada del proyecto del **[Curso de Python Intermedio para Entornos virtuales y PEP8](https://platzi.com/cursos/python-entornos-virtuales/)** de Platzi (profesor Luis Martínez).
Fork de [platzi/python-intermedio](https://github.com/platzi/python-intermedio). Mis notas están en la rama `comentarios-y-ruff`.
 
---
 
## 🎯 Resumen
 
Es una **app de consola** que:
 
1. **Busca noticias** en [NewsAPI](https://newsapi.org/) sobre un tema (por defecto, "Python").
2. **Le envía las noticias a OpenAI** (modelo `gpt-4o`) junto con una pregunta.
3. **Imprime en la terminal** una respuesta breve en español.
El objetivo del curso no es la app en sí, sino escribir **código profesional**: legible (PEP 8 + Ruff), bien organizado (módulos y paquetes), con manejo de errores, tipado y documentación, y aislado en un entorno virtual.
 
---
 
## 🗂️ Estructura
 
```
python-intermedio/
├── main.py              # Punto de entrada: busca noticias y las analiza con IA
├── news_analyzer/       # Paquete principal de la app
│   ├── __init__.py      # Convierte la carpeta en paquete
│   ├── config.py        # Lee las claves del archivo .env y define la URL de NewsAPI
│   ├── api_client.py    # Clientes de noticias (NewsAPI real, The Guardian de ejemplo)
│   ├── exceptions.py    # Errores propios: NewsSystemError → APIKeyError
│   ├── utils.py         # Funciones de apoyo: limpiar texto, filtrar, tiempo de lectura
│   └── open_ia.py       # Envía las noticias a OpenAI y muestra la respuesta
├── examples/            # Ejemplos sueltos de cada tema del curso
│   ├── pep_8.py         # Reglas de estilo
│   ├── comprehensions.py
│   ├── f_strings.py
│   ├── args_kwargs.py
│   ├── try_except.py
│   ├── type_hints.py
│   ├── docstrings.py
│   ├── numerate.py      # enumerate
│   ├── filter_pairs.py  # filter
│   ├── maps.py          # map
│   └── sample_data.py   # Noticias de prueba
├── pyproject.toml       # Datos del proyecto y dependencias (lo usa uv)
├── uv.lock              # Versiones exactas instaladas
├── .python-version      # Versión de Python del proyecto (3.13)
└── .vscode/settings.json  # Ruff formatea y ordena imports al guardar
```
 
---
 
## 🔄 Cómo fluye el programa
 
```
main.py
  │ 1. config.py lee API_KEY desde .env
  │ 2. fetch_news("newapi", api_key=..., query="Python")   ← api_client.py
  │        └─ elige newsapi_client y le pasa los argumentos con *args/**kwargs
  │        └─ si NewsAPI falla → lanza APIKeyError         ← exceptions.py
  │ 3. si hay noticias → analyze_news_with_ia(articles, pregunta)  ← open_ia.py
  │        └─ arma un prompt con máximo 10 noticias y lo envía a gpt-4o
  ▼
Respuesta impresa en la terminal
```
 
---
 
## ▶️ Cómo ejecutarlo
 
```bash
cd /home/jasonquiar/proyectos/platzi/python-intermedio
uv sync                      # crea .venv e instala openai, python-dotenv y ruff
```
 
Crea un archivo `.env` (no se sube a GitHub, lo ignora `.gitignore`):
 
```
API_KEY=tu_clave_de_newsapi
OPENAI_API_KEY=tu_clave_de_openai
```
 
Ejecuta:
 
```bash
uv run python main.py        # la app completa
uv run python examples/f_strings.py   # un ejemplo suelto
uv run ruff format .         # formatea todo el proyecto
uv run ruff check .          # revisa errores y malas prácticas
```
 
---
 
## 📖 Glosario
 
| Término | Qué es (en corto) | Dónde aparece | Clase |
| --- | --- | --- | --- |
| **PEP 8** | Guía oficial de estilo de Python: nombres, espacios, orden de imports. | `examples/pep_8.py` | 02 |
| **Ruff** | Formateador y linter muy rápido que aplica PEP 8 por ti. | `.vscode/settings.json` | 02 |
| **Linter** | Herramienta que revisa el código y avisa de errores o malas prácticas sin ejecutarlo. | `ruff check` | 02 |
| **snake_case** | Nombres en minúscula con guion bajo: `fetch_news`. Para funciones y variables. | Todo el proyecto | 02 |
| **Constante** | Valor que no debería cambiar; se escribe en MAYÚSCULAS: `BASE_URL`. | `config.py` | 02 |
| **Comprehension** | Crear una lista, set o dict en una línea a partir de otra colección. | `utils.py` (`get_unique_sources`) | 03-04 |
| **f-string** | Texto con variables adentro: `f"Hola {nombre}"`. | `open_ia.py` (prompt) | 05-06 |
| **`*args`** | Recibe cualquier cantidad de argumentos posicionales como una tupla. | `fetch_news` | 07 |
| **`**kwargs`** | Recibe argumentos con nombre como un diccionario. | `fetch_news` | 08 |
| **API** | Servicio al que tu código le pide datos por internet. | NewsAPI, OpenAI | 09 |
| **API key** | Clave secreta que identifica quién usa la API. | `.env` | 09 |
| **JSON** | Formato de texto para intercambiar datos; en Python se vuelve `dict`/`list`. | `api_client.py` | 09 |
| **`try` / `except`** | Intenta algo y, si falla, maneja el error sin que el programa se caiga. | `main.py`, `api_client.py` | 10 |
| **`finally`** | Bloque que se ejecuta siempre, haya error o no. | `examples/try_except.py` | 11 |
| **Excepción personalizada** | Clase de error propia que hereda de `Exception`. | `exceptions.py` | 12 |
| **Type hints** | Etiquetas que dicen qué tipo espera y devuelve una función: `-> str`. | `utils.py`, `open_ia.py` | 13-14 |
| **Docstring** | Documentación entre triples comillas al inicio de una función, clase o archivo. | Todos los módulos | 15 |
| **Entorno virtual (`.venv`)** | Carpeta aislada con su propio Python y librerías, una por proyecto. | `.venv/` | 16-18 |
| **uv** | Herramienta de Astral que crea entornos e instala dependencias muy rápido. | `pyproject.toml`, `uv.lock` | 19 |
| **Dependencia** | Librería externa que el proyecto necesita (ej.: `openai`). | `pyproject.toml` | 19 |
| **Módulo** | Un archivo `.py` que puedes importar desde otro. | `config.py`, `utils.py`… | 20 |
| **Paquete** | Carpeta con módulos y un `__init__.py`. | `news_analyzer/` | 21 |
| **`enumerate`** | Recorre una lista entregando posición y valor a la vez. | `examples/numerate.py` | 22 |
| **`filter`** | Deja solo los elementos que cumplen una condición. | `get_articles_by_source` | 23 |
| **`lambda`** | Función pequeña y sin nombre, escrita en una línea. | `get_articles_by_source` | 23 |
| **`map`** | Aplica una función a cada elemento de una colección. | `examples/maps.py` | 24 |
| **`.env` / dotenv** | Archivo con claves secretas que `python-dotenv` carga al entorno. | `config.py`, `open_ia.py` | 25 |
| **Prompt** | Instrucción o pregunta que se le envía a un modelo de IA. | `open_ia.py` | 25 |
 
---
 
## 🔍 Detalles que noté en el código
 
- `guardian_client` es solo de **ejemplo**: devuelve un texto, no consulta The Guardian de verdad.
- `analyze_news_with_ia` **imprime** la respuesta, pero no la devuelve (retorna `None`). Por eso en `main.py` el `print(...)` muestra también `None` al final.
- El nombre del cliente se escribe `"newapi"` (sin la "s"), aunque el servicio se llama NewsAPI.
- `process_article_data` está vacía a propósito: es un espacio para completar.
