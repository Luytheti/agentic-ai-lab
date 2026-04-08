import re
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# -------- STEP 1 --------
def extract_numbers(text):
    numbers = re.findall(r'\d+', text)
    return [int(n) for n in numbers]


# -------- STEP 2 --------
def compute_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


# -------- STEP 3 --------
def summarize_result(result):
    prompt = f"Summarize this result in one sentence: {result}"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content