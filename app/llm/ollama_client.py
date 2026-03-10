import ollama


def ask_llm(context, question):

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]