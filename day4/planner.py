import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_plan(query):
    prompt = f"""
    You are a planning agent.

    Break the task into steps using ONLY these tools:
    - extract_numbers
    - compute_average
    - summarize_result

    Return ONLY steps (one per line, no explanation).

    Example:
    extract_numbers
    compute_average
    summarize_result

    Query: {query}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    plan_text = response.choices[0].message.content.strip()

    # clean parsing
    steps = []
    for line in plan_text.split("\n"):
        step = line.strip().lower()
        if step in ["extract_numbers", "compute_average", "summarize_result"]:
            steps.append(step)

    return steps