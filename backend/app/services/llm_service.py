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

        First, determine the main subject or topic of the provided context.

        Then evaluate whether the question is related to that subject.

        If the question is clearly unrelated to the subject of the context,
        respond exactly with:
        "The answer is not in the material."

        If the question is related to the subject:
        - If the answer is directly stated in the context, use the context.
        - If the answer is not directly stated but is clearly about the same subject,
        use your own general knowledge to provide a clear and accurate answer.

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
