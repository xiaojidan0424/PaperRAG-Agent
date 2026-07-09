import os
from openai import OpenAI


api_key = os.getenv(
    "DEEPSEEK_API_KEY"
)


if api_key is None:
    raise ValueError(
        "Please set DEEPSEEK_API_KEY in .env"
    )


client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)


# ==========================
# RAG Generation
# ==========================


def generate_answer(
        query,
        context
):


    prompt = f"""
You are an AI assistant specialized in academic paper analysis.

Answer the question based ONLY on the provided context.

Requirements:

1. Do not use external knowledge.
2. If the answer is unavailable, clearly state:
"I don't know based on the provided context."
3. Provide concise but complete academic explanations.


Context:

{context}


Question:

{query}


Answer:

"""



    response = client.chat.completions.create(

        model="deepseek-chat",

        messages=[

            {

                "role":"user",

                "content":prompt

            }

        ],

        temperature=0.2

    )



    return response.choices[0].message.content