import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_answer(question: str, context_chunks: list[str]) -> str:
    """
    Generate grounded answer using retrieved context.
    """

    context_text = "\n\n".join(
        [
            f"[Chunk {item['chunk_id']}] {item['chunk']}"
            for item in context_chunks
        ]
    )


    prompt = f"""
    You are a helpful academic assistant.

    Use ONLY the context below to answer the question.
    Reference chunk numbers if helpful.
    Only say the answer is not in the material if it is completely unrelated.

    Context:
    {context_text}

    Question:
    {question}

    Answer:
    """


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
