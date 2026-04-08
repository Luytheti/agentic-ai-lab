import random
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# Calculator
def calculator(expression):
    try:
        # safer eval (basic protection)
        allowed_chars = "0123456789+-*/(). "
        if any(char not in allowed_chars for char in expression):
            return "Invalid expression"

        result = eval(expression)
        return f"Result: {result}"

    except Exception:
        return "Error in calculation"


# Weather
def weather(city):
    mock_weather = {
        "mumbai": "30°C, Humid",
        "delhi": "25°C, Clear sky",
        "london": "15°C, Cloudy",
        "new york": "18°C, Windy",
        "nagpur": "40°C, Sunny",
    }

    city = city.lower()

    if city in mock_weather:
        return f"Weather in {city.title()}: {mock_weather[city]}"
    else:
        temp = random.randint(20, 35)
        return f"Weather in {city.title()}: {temp}°C, Partly Cloudy"


# Summary
def summarize_text(text):
    prompt = f"Summarize this in 2-3 sentences:\n{text}"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content