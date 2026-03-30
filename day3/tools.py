from datetime import datetime
import random
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def calculator(expression):
    try:
        result = eval(expression)
        return f"Result: {result}"
    except:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": expression}]
        )
        return response.choices[0].message.content

def weather(city):
    mock_weather = {
        "mumbai": "30°C, Humid",
        "delhi": "25°C, Clear sky",
        "london": "15°C, Cloudy",
        "new york": "18°C, Windy",
        "nagpur": "40°C, Sunny",
        "muscat": "24°C, Rainy",
        "dubai": "34°C, Cloudy",
        "washington": "2°C, Hailstorm", 
        "florida": "12°C, Thunderstorm",
        "tel-aviv": "34°C, Sunny"
    }
    city = city.lower()
    if city in mock_weather:
        return f"Weather in {city.title()}: {mock_weather[city]}"
    else:
        temp = random.randint(20, 35)
        return f"Weather in {city.title()}: {temp}°C, Partly Cloudy"

def summarize_text(text):
    prompt = f"""
    Summarize the following text in 2-3 sentences.
    Text:
    {text}
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content