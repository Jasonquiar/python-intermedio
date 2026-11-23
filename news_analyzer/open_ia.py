"""Funciones de análisis de noticias mediante la API de OpenAI."""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def analyze_news_with_ia(articles: list[dict], query: str) -> str | None:
    """Envía noticias y una pregunta al modelo e imprime su respuesta.

    Se incluyen como máximo diez noticias y hasta cien caracteres de descripción
    por noticia para limitar el tamaño del contexto enviado. La función imprime
    el resultado; actualmente no devuelve un valor.
    """

    client = OpenAI(
        # Si se omite, el cliente también puede leer la clave del entorno.
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    context = "\n".join(
        [
            f"- {article['title']}: {article.get('description', '')[:100]}..."
            for article in articles[:10]  # Limitar para control de costos
        ]
    )

    # El prompt combina el contexto seleccionado con la pregunta del usuario.
    prompt = f"""
        Basándote en estas noticias:
        {context}

        Pregunta: {query}

        Responde de forma concisa en español.
    """

    print(prompt)

    response = client.responses.create(
        model="gpt-4o",
        instructions="Eres un agente que lee contexto y responde de manera breve",
        input=prompt,
    )

    print(response.output_text)